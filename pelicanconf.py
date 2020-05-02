#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoxMaSk'
SITENAME = 'Le Free de la Passion'
SITESUBTITLE = 'La passion de la liberté'

SITEURL = 'https://foxmask.net'
TIMEZONE = 'Europe/Paris'

THEME = '/home/foxmask/Projects/foxmask.net/pelican-themes/pelican-bootstrap3/'


PATH = 'content'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
#TAG_FEED_RSS = 'feeds/{slug}.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
#TAG_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10

# theme bootstrap https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
BANNER_SUBTITLE = 'La passion de la liberté'
BANNER = '/static/banner.jpg'
DISPLAY_TAGS_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

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
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5

USE_OPEN_GRAPH = True

CUSTOM_LICENSE='Unless otherwise stated, all articles are published under the <a href="http://www.wtfpl.net/about/">WTFPL</a> license.'

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')

# Standard
DEFAULT_CATEGORY = 'General'

ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

LINKS = (
         ('RSS', 'https://foxmask.net/feeds/all.rss.xml'),
         ('Atom', 'https://foxmask.net/feeds/all.atom.xml'),
         )

FREE_PROJECT = True

ATOM = (('ATOM Python', 'https://foxmask.net/feeds/python.atom.xml'),
       ('ATOM Django', 'https://foxmask.net/feeds/django.atom.xml'),)
RSS = (('RSS Python', 'https://foxmask.net/feeds/python.rss.xml'),
       ('RSS Django', 'https://foxmask.net/feeds/django.rss.xml'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}

PLUGIN_PATHS = ['/home/foxmask/Projects/foxmask.net/pelican-plugins']

PLUGINS = ['sitemap', 'pelican-page-order', 'tag_cloud', 'github_activity', 'related_posts', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code',
           'neighbors', 'github_activity', 'tipue_search', 'i18n_subsites']

RELATED_POSTS_MAX = 8

# for the plugin sitemap
SITEMAP = {'format': 'xml'}

DISQUS_SITENAME = "foxmasktriggerhappyeu"

CATEGORY_IN_SIDEBAR = True


FEED_DOMAIN = 'https://foxmask.net'
FEED_ATOM = 'main.atom.xml'
FEED_RSS = 'main.rss.xml'

GITHUB_ACTIVITY_FEED = 'https://github.com/foxmask.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables':{},
    },
    'output_format': 'html5',
}
