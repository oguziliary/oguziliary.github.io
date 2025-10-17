AUTHOR = 'oux'
SITENAME = 'oğuziliary'
SITEURL = ''

PATH = "content"
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Berlin'

# Primary language for the root site
DEFAULT_LANG = 'tr'
if DEFAULT_LANG == 'tr':
    LOCALE = ('tr_TR.UTF-8', 'C.UTF-8', 'tr_TR')
else:
    LOCALE = ('en_US.UTF-8', 'C.UTF-8', 'en_US')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (

)

# Social widget
SOCIAL = (
    ("goodreads", "https://www.goodreads.com/mroximut"),
)

DEFAULT_PAGINATION = 10

# Plugins
PLUGINS = ['render_math', 'i18n_subsites']

# Show untranslated content in both languages
I18N_UNTRANSLATED_ARTICLES = 'keep'
I18N_UNTRANSLATED_PAGES = 'keep'

# Simple dictionary-based translations used in templates
TEXTS = {
    'en': {
        'nav_posts': 'Things I happen to have written',
        'read_more': 'Read →',
        'from_date': 'from',
        'by_on': 'by {author} on {date}',
        'newer': '← Newer',
        'older': 'Older →',
    },
    'tr': {
        'nav_posts': 'Yazmıştı olduklarım',
        'read_more': 'Oku →',
        'from_date': 'tarihinden',
        'by_on': '{author} tarafından {date} tarihinde',
        'newer': '← Yeni',
        'older': 'Eski →',
    },
}

# Generate a subsite only for the non-default language
if DEFAULT_LANG == 'tr':
    LANG = 'tr'
    I18N_SUBSITES = {
        'en': {
            'SITENAME': 'oguziliary',
            'LANG': 'en',
            'LOCALE': ('en_US.UTF-8', 'C.UTF-8', 'en_US'),
        },
    }
else:
    LANG = 'en'
    I18N_SUBSITES = {
        'tr': {
            'SITENAME': 'oğuziliary',
            'LANG': 'tr',
            'LOCALE': ('tr_TR.UTF-8', 'C.UTF-8', 'tr_TR'),
        },
    }

# Localized date formats per language (Python strftime)
DATE_FORMATS = {
    'en': '%B %d, %Y',      # e.g., September 21, 2025
    'tr': '%d %B %Y',       # e.g., 21 Eylül 2025
}


THEME = "mytheme"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
