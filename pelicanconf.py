#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoxMaSk'
SITENAME = 'FoxMaSk - Le Free de la Passion'
SITESUBTITLE = 'La passion de la liberté'

SITEURL = 'http://foxmask.trigger-happy.eu'
TIMEZONE = 'Europe/Paris'

THEME = 'pelican-octopress-theme'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


DEFAULT_CATEGORY = 'General'

ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = (('Sam&Max', 'http://sametmax.com'),
         ('Trigger Happy', 'http://trigger-happy.eu'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (('@foxmask GitHub', 'https://github.com/foxmask'),)

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS = ['tag_cloud', 'read_more_link', 'related_posts',
#           'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube',
#           'liquid_tags.vimeo', 'liquid_tags.include_code']
PLUGINS = ['related_posts', 'liquid_tags.img', 'liquid_tags.video', 
           'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code',
           'neighbors', 'github_activity']

# related_posts plugin - https://github.com/getpelican/pelican-plugins/tree/master/related_posts
RELATED_POSTS_MAX = 5

# Following items are often useful when publishing

DISQUS_SITENAME = "foxmasktriggerhappyeu"
#GOOGLE_ANALYTICS = ""

# pour le theme octopress
SIDEBAR_IMAGE = '/static/cactus.png'
SEARCH_BOX = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_FEEDS_ON_MENU = True
#GITHUB_USER = "foxmask"
#GITHUB_REPO_COUNT = 5
#GITHUB_SKIP_FORK = False
#GITHUB_SHOW_USER_LINK = False

CATEGORY_IN_SIDEBAR = False


FEED_DOMAIN = 'http://foxmask.trigger-happy.eu'
FEED_ATOM = 'main.atom.xml'
FEED_RSS = 'main.rss.xml'

# https://github.com/getpelican/pelican-plugins/tree/master/github_activity
GITHUB_ACTIVITY_FEED = 'https://github.com/foxmask.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10
