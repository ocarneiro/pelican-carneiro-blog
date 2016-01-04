#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Otávio Carneiro'
SITENAME = 'Só mais um Carneiro'
SITEURL = 'http://carneiro.blog.br/um'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Calango Hacker Clube', 'http://calango.club/'),
         ('Jerônimo', 'http://www.blogdoje.com.br/'),
         ('Phil Jones', 'http://tecno-artesanato.tumblr.com/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/ocarneiro/'),
          ('Twitter', 'https://twitter.com/carneiroblogbr'),
          ('YouTube', 'https://www.youtube.com/user/UmCarneiro/feed'),
         )

TWITTER_USERNAME = 'so1carneiro'
GITHUB_URL = 'https://github.com/ocarneiro/'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme conf
THEME = "themes/carneirospill"
#theme based on waterspill: 
#https://github.com/getpelican/pelican-themes/tree/master/waterspill

#Habilitar quando houver páginas a mostrar
DISPLAY_PAGES_ON_MENU = False

#Ativar a tag cloud (nuvem de tags)
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_STEPS = 4
TAG_CLOUD_SORTING = 'alphabetically'
