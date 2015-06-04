#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Otávio Carneiro'
SITENAME = 'Só mais um Carneiro'
SITEURL = 'http://carneiro.blog.br/um'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

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
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme conf
THEME = "themes/carneirospill"
#theme based on waterspill: 
#https://github.com/getpelican/pelican-themes/tree/master/waterspill
