BadgeBot
--------

A twitter bot that retweets your Fedora Badges!

Try it out
----------

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

Systemd
-------

You can run it under systemd for 24hour badge twittification!  Check out
``install.sh``::

    $ sudo ./install.sh && sudo journalctl -u badgebot --follow
    + cp badgebot.py /usr/local/bin/badgebot.py
    + cp /home/threebean/devel/badgebot/badgebot.service /usr/lib/systemd/system/badgebot.service
    + cp fedmsg.d/badgebot-basics.py fedmsg.d/twitter-secrets.py /etc/fedmsg.d/.
    + systemctl daemon-reload
    + systemctl restart badgebot
    -- Logs begin at Sun 2013-07-28 07:27:21 CDT. --
    Aug 04 16:07:47 radek systemd[1]: Starting A Twitter bot for your Fedora Badges.  Wow....
    Aug 04 16:07:47 radek systemd[1]: Started A Twitter bot for your Fedora Badges.  Wow..
    Aug 04 16:07:48 radek badgebot.py[9155]: Setting up twitter connection.
    Aug 04 16:07:48 radek badgebot.py[9155]: Looking for messages with 'fedbadges' in the topic
    Aug 04 16:07:48 radek badgebot.py[9155]: Relating to any user at all!
    Aug 04 16:07:48 radek badgebot.py[9155]: Posting up to listen on the fedmsg bus.  Waiting for a message...
