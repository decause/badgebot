#!/bin/bash -x
# install.sh - (re)install and (re)start the badgebot

# Install our script
cp badgebot.py /usr/local/bin/badgebot.py

# Make sure no one else can read our secrets.
cp fedmsg.d/twitter-scripts.py /etc/fedmsg.d/.
chown fedmsg:fedmsg /etc/fedmsg.d/twitter-secrets.py
chmod o-r /etc/fedmsg.d/twitter-secrets.py

# Copy in service file for systemd
cp badgebot.service /usr/lib/systemd/system/badgebot.service
systemctl daemon-reload
systemctl restart badgebot
