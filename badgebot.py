import os
import fedmsg
import fedmsg.meta
import requests
import fabulous
from fabulous.image import Image
import urllib
import tempfile
import subprocess


config = fedmsg.config.load_config()
fedmsg.meta.make_processors(**config)

#fedoratagger.tag.create -- decause added tag "bmp" to tuxpaint https://apps.fedoraproject.org/tagger/tuxpaint


for name, endpoint, topic, msg in fedmsg.tail_messages():
    #if not topic.startswith("org.fedoraproject.prod.fedoratagger.tag"):
    #    continue
    if 'stg' in endpoint:
        continue
    print name, endpoint

    icon = fedmsg.meta.msg2icon(msg, **config)
    icon2 = fedmsg.meta.msg2secondary_icon(msg, **config)
    subtitle = fedmsg.meta.msg2subtitle(msg, **config)
    link = fedmsg.meta.msg2link(msg, **config)


    response = requests.get('http://da.gd/s', params=dict(url=link))
    link = response.text.strip()

    _, tmp = tempfile.mkstemp()
    urllib.urlretrieve(icon, tmp)

    _, tmp2 = tempfile.mkstemp()
    urllib.urlretrieve(icon2, tmp2)

    cmd = 'montage -background black -adjoin %s %s kittens-together.jpg' % (icon, icon2)

    process = subprocess.Popen(cmd.split())
    result = process.communicate()
    print result

    try:
        print Image('kittens-together.jpg', width=80)
    except IOError:
        pass

    os.remove(tmp)
    os.remove(tmp2)
    os.remove('kittens-together.jpg')

    print subtitle, link

    # Bail out after one message..
    import sys
    sys.exit(0)

