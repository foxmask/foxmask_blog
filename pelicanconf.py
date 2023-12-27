#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoxMaSk'
SITENAME = 'Le Free de la Passion'
SITESUBTITLE = 'La passion de la liberté'
SITELOGO='https://foxmask.eu.org/static/cactus.png'
DEFAULT_METADATA = {"Le Free de la Passion": "La passion de la liberté"}

# SITEURL = 'https://foxmask.github.io'
SITEURL = 'https://foxmask.eu.org'
TIMEZONE = 'Europe/Paris'

THEME = '/home/foxmask/Projects/foxmask.eu.org/foxmask_blog/Flex/'


PATH = 'content'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#TAG_FEED_RSS = 'feeds/{slug}.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
#TAG_FEED_ATOM = 'feeds/{slug}.atom.xml'
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
#FEED_MAX_ITEMS = 100

# theme bootstrap https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
BANNER_SUBTITLE = 'La passion de la liberté'
#BANNER = '/static/banner.jpg'
#DISPLAY_TAGS_ON_SIDEBAR = True
#BOOTSTRAP_NAVBAR_INVERSE = True

#DISPLAY_ARTICLE_INFO_ON_INDEX = True

#ARCHIVES_SAVE_AS = 'archives.html'
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

#DISPLAY_TAGS_INLINE = True
#TAG_CLOUD_MAX_ITEMS = 20
#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_CATEGORIES_ON_MENU = True
#DISPLAY_FEEDS_ON_MENU = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
#RECENT_POST_COUNT = 5

#USE_OPEN_GRAPH = True

#CUSTOM_LICENSE='Unless otherwise stated, all articles are published under the <a href="http://www.wtfpl.net/about/">WTFPL</a> license.'

#DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')

# Standard
DEFAULT_CATEGORY = 'Main'

#ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
#ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
#PAGE_URL = 'pages/{slug}'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'

#LINKS = (
#         ('FoxMaSk RSS', '/feeds/all.rss.xml'),
#         ('Python', 'https://python.org/'),
#         ('PyConFr', 'https://pycon.fr/'),
#         ('PyConKr', 'https://pycon.kr/'),
#         ('Django', 'https://www.djangoproject.com/'),
#        ('DRF', 'https://www.django-rest-framework.org/'),
#        ('Ansible', 'https://www.ansible.com/'),
#        ('Centre Culturel Coréen', 'https://www.coree-culture.org/?lang=fr'),
#)

SOCIAL = (
        ("Framapiaf - Mastodon Fr", "https://framapiaf.org/"),
        ("BdxTown - Akkoma Fr", "https://bdx.town/"),
        ("Planet Moe - Mastodon Kr", "https://planet.moe"),
)        

#FREE_PROJECT = True

#RSS = (('RSS Python', '/feeds/python.rss.xml'),
#       ('RSS Django', '/feeds/django.rss.xml'),
#       ('RSS Korea', '/feeds/korea.rss.xml'),
#      )

#DEFAULT_PAGINATION = 10

STATIC_PATHS = ['static']

#EXTRA_PATH_METADATA = {
#    'static/robots.txt': {'path': 'robots.txt'},
#    'static/favicon.ico': {'path': 'favicon.ico'},
#}

#PLUGIN_PATHS = ['/home/foxmask/Projects/foxmask.net/pelican-plugins']

#PLUGINS = ['sitemap', 'pelican-page-order', 'tag_cloud',
#           'related_posts', 'liquid_tags', 'neighbors', 'tipue_search', 'i18n_subsites']

#RELATED_POSTS_MAX = 8

#SITEMAP = {'format': 'xml'}

#CATEGORY_IN_SIDEBAR = True

#FEED_DOMAIN = 'https://www.foxmask.org'
#FEED_ATOM = 'main.atom.xml'
#FEED_RSS = 'main.rss.xml'


#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables':{},
    },
    'output_format': 'html5',
}

GITHUB_URL = "https://git.afpy.org/foxmask/"

PYGMENTS_STYLE = "monokai"

CC_LICENCE = {
        "name": "Do What the Fuck You Want to Public License",
        "version": "2.0",
        "slug": "wtfpl"
        }
