#!/usr/bin/env python

import os
import sys
import tempfile
import urllib

import tweepy
import fedmsg
import fedmsg.meta

config = fedmsg.config.load_config()
fedmsg.meta.make_processors(**config)

consumer_key        = config['consumer_key']
consumer_secret     = config['consumer_secret']
access_token_key    = config['access_token_key']
access_token_secret = config['access_token_secret']

auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_handler.set_access_token(access_token_key, access_token_secret)
twitter_api = tweepy.API(auth_handler)


badgebot_topic_filter = config.get('badgebot_topic_filter')
badgebot_username = config.get('badgebot_fas_username')

# This is mandatory, otherwise we'll get banned from twitter.
if not badgebot_topic_filter:
    print "No 'badgebot_topic_filter' found in the fedmsg config.  Bailing."
    sys.exit(3)

print "Looking for messages with %r in the topic" % badgebot_topic_filter
if badgebot_username:
    print "  Relating to the user %r" % badgebot_username
else:
    print "  Relating to any user at all!"

for name, endpoint, topic, msg in fedmsg.tail_messages():
    if badgebot_topic_filter not in topic:
        continue

    if badgebot_username:
        users = fedmsg.meta.msg2usernames(msg, **config)
        if badgebot_username not in users:
            print "%r is not among %r" % (badgebot_username, users)
            continue
    else:
        print "'badgebot_fas_username' not specified.  Proceeding."

    # So, we know we have a fedbadges message and that it is for us.
    icon = fedmsg.meta.msg2icon(msg, **config)
    subtitle = fedmsg.meta.msg2subtitle(msg, **config)
    link = fedmsg.meta.msg2link(msg, **config)
    print "Got %r" % subtitle

    # We're just assuming here that the image is a png.  If its not, then
    # twitter is probably going to freak out on us later.
    _, filename = tempfile.mkstemp(suffix='.png')
    print "Downloading", icon, "to", filename
    urllib.urlretrieve(icon, filename)

    # Now construct and post our tweet.
    content = subtitle + " " + link
    print "Tweeting %r" % content
    twitter_api.update_with_media(filename, content)

    print "Cleaning up %r" % filename
    os.remove(filename)

    print "Done.  Going back to listen on fedmsg."
