# -*- coding: utf-8 -*- #

AUTHOR = u"haridas"
SITENAME = u"haridas.in"
# Don't, change the current URL scheme.
SITEURL = 'http://haridas.in'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Pagination settings.
DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 2

# Theme settings.
THEME = '/mnt/data/projects/github/haridas.github.com/src/templates/notmyidea'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

# Ordering of content.
REVERSE_ARCHIVE_ORDER = True

# Other menu items
MENUITEMS = [('Archives', '/archives.html')]

## External services and Social medias.

DISQUS_SITENAME = 'haridas'
GITHUB_URL = 'http://github.com/haridas'
GOOGLE_ANALYTICS = 'UA-23592173-1'
TWITTER_USERNAME = 'haridas_n'

# Blogroll
LINKS = (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
         )

# Social widget
SOCIAL = (
        ('twitter', 'http://twitter.com/haridas_n'),
        ('github', 'http://github.com/haridas'),
        ('linkedin', 'http://in.linkedin.com/pub/haridas-n/19/95/825'),
         )

ARTICLE_EXCLUDES = ['templates', 'pages']
PAGE_EXCLUDES = ['articles', 'drafts', 'pages']
