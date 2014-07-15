BadgeBot
--------

A twitter bot that retweets your Fedora Badges!

----

To try it out, first install the dependencies::

    $ yum install tweepy fedmsg python-fedmsg-meta-fedora-infrastructure

Then, copy ``fedmsg.d/twitter-secrets.py.example`` to
``fedmsg.d/twitter-secrets.py``.  Open it in your editor::

    config = dict(
        consumer_key        = "abcdefg12345678",
        consumer_secret     = "abcdefg12345678",
        access_token_key    = "abcdefg12345678",
        access_token_secret = "abcdefg12345678",
    )

You'll need to visit https://dev.twitter.com and create an 'application' in
order to get these api keys.

Also, take a look at ``fedmsg.d/badgebot-basics.py``::

    config = dict(

        # Only tweet fedmsg messages with this in the topic
        badgebot_topic_filter='fedbadges',

        # Only tweet fedmsg messages that have to do with this person.
        # If it is the None value, then just tweet about everyone.
        badgebot_fas_username=None, # 'ralph',
    )

Finally, run the script::

    $ python badgebot.py
