#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoxMaSk'
SITENAME = 'Le Free de la Passion'
SITESUBTITLE = 'La passion de la liberté'

SITEURL = 'https://foxmask.trigger-happy.eu'
TIMEZONE = 'Europe/Paris'

THEME = '../pelican-themes/pelican-bootstrap3/'


PATH = 'content'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10

CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# theme bootstrap https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
BANNER_SUBTITLE = 'La passion de la liberté'
BANNER = '/static/banner.jpg'
DISPLAY_TAGS_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True

GITHUB_USER = "foxmask"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False

DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 20
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_FEEDS_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

TWITTER_CARDS = True
TWITTER_USERNAME = 'triggerhappyeu'
TWITTER_WIDGET_ID = 669143142793412608

CUSTOM_LICENSE='Unless otherwise stated, all articles are published under the <a href="http://www.wtfpl.net/about/">WTFPL</a> license.'

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')
TIPUE_SEARCH = True
SEARCH_URL = 'search.html'

AVATAR = '/static/cactus.png'

ABOUT_ME = '<a href="/pages/a-propos">Passionné par les Logiciels Libres</a><br/><a href="https://twitter.com/foxxmask/">@foxxmask</a>'

# Standard
DEFAULT_CATEGORY = 'General'

ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Blogroll
LINKS = (('Sam&Max', 'http://sametmax.com'),
         ('S&M Community news', 'https://smcomm.trigger-happy.eu/'),
         ('Indexerror Q&R Python', 'http://indexerror.net/'),
         )

FREE_PROJECT = True

# Social widget
# SOCIAL = (('@foxmask GitHub', 'https://github.com/foxmask'),)
# SOCIAL = (('Twitter', 'https://twitter.com/triggerhappyeu'),)

ATOM = (('ATOM Python', 'https://foxmask.trigger-happy.eu/feeds/python.atom.xml'),
       ('ATOM Django', 'https://foxmask.trigger-happy.eu/feeds/django.atom.xml'),)
RSS = (('RSS Python', 'https://foxmask.trigger-happy.eu/feeds/python.rss.xml'),
       ('RSS Django', 'https://foxmask.trigger-happy.eu/feeds/django.rss.xml'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'pelican-page-order', 'tag_cloud', 'github_activity', 'related_posts', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code',
           'neighbors', 'github_activity', 'tipue_search']

# related_posts plugin - https://github.com/getpelican/pelican-plugins/tree/master/related_posts
RELATED_POSTS_MAX = 5

# Following items are often useful when publishing

# for the plugin sitemap
SITEMAP = {'format': 'xml'}

DISQUS_SITENAME = "foxmasktriggerhappyeu"

# pour le theme octopress
#SIDEBAR_IMAGE = '/static/cactus.png'
#SEARCH_BOX = True
#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_CATEGORIES_ON_MENU = True
#DISPLAY_FEEDS_ON_MENU = True

CATEGORY_IN_SIDEBAR = False


FEED_DOMAIN = 'https://foxmask.trigger-happy.eu'
FEED_ATOM = 'main.atom.xml'
FEED_RSS = 'main.rss.xml'

# https://github.com/getpelican/pelican-plugins/tree/master/github_activity
GITHUB_ACTIVITY_FEED = 'https://github.com/foxmask.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10
