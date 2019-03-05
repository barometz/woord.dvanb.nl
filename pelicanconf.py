#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dominic van Berkel'
SITENAME = 'woord'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['plugin']
PLUGINS = ['filetime_from_git', 'open_graph', 'i18n_subsites']

THEME = 'theme/pelican-bootstrap3'
BOOTSTRAP_THEME = 'yeti'

# bootstrap3 settings
DISPLAY_ARTICLE_INFO_ON_INDEX = False
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = False
DOCUTIL_CSS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = () # (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/baudvine'),
          ('GitHub', 'https://github.com/barometz/'),
          ('LinkedIn', 'https://www.linkedin.com/in/dvberkel/'),)

TWITTER_USERNAME = 'baudvine'
TWITTER_CARDS = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_SUBSITES = {
    'nl': { },
}


