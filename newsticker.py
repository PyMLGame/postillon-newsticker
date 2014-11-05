#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Postillon Newsticker for Mate Light
"""

__author__ = 'Ricardo Band'
__copyright__ = 'Copyright 2014, Ricardo Band'
__credits__ = ['Ricardo Band']
__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'Ricardo Band'
__email__ = 'me@xengi.de'
__status__ = 'Production'

import time
import socket
import random
from html.parser import HTMLParser

import feedparser


xml = feedparser.parse('http://feeds.feedburner.com/blogspot/rkEL?format=xml')
# this crazy thing takes all news articles (a) and get all news lines from
# each article (b). The sum() function does the magic and transforms the list:
# [a=[b, b, b], a=[b, b, b]]
# to this list:
# [b, b, b, b, b, b]
# I have no idea why this works but it does it's job.
feed = sum([[HTMLParser().unescape(n)
             for n in i.description.split('<br>') if n.startswith('+++')]
            for i in xml.entries if i.title.startswith('Newsticker')], [])

selection = random.sample(feed, 3)
for news in selection:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('matelight', 1337))
    sock.send(bytes(news, 'UTF-8'))
    sock.close()
    time.sleep(1)
