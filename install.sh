#!/bin/bash -x

cp badgebot.py /usr/local/bin/badgebot.py
cp /home/threebean/devel/badgebot/badgebot.service /usr/lib/systemd/system/badgebot.service
cp fedmsg.d/*.py /etc/fedmsg.d/.
systemctl daemon-reload
systemctl restart badgebot
