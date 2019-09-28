#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import werobot

from GoogleScraper import scrape_with_config, GoogleSearchError
from socket import error as SocketError


CONFIG = {
    'do_caching': False,
    'keyword': '',
    'num_pages_for_keyword': 1,
    'scrape_method': 'http',
    'search_engines': ['baidu'],
    'use_own_ip': True
}

robot = werobot.WeRoBot(token='MbGwtIXuRYLmXiLjXmBrb9Q')


class Content:
    link = 'link'
    snippet = 'snippet'
    title = 'title'


def search(data):
    global CONFIG

    CONFIG['keyword'] = data

    try:
        result = scrape_with_config(CONFIG)
    except (GoogleSearchError, SocketError) as _:
        return 'Not found'

    buf = []

    for serp in result.serps:
        for link in serp.links:
            if link.snippet is not None:
                buf.append(link.snippet.strip()+os.linesep)

    return os.linesep.join(buf)


@robot.text
def response(msg):
    return search(msg.content)


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()
