#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Frank Hrach IV'
SITENAME = 'HrachBlog'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('About', 'about.md://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/')
          )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/fhrach4'),
          ('GitHub', 'https://www.github.com/fhrach4'),)

DEFAULT_PAGINATION = 10

# Theme
THEME = 'pelican-blueidea'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
