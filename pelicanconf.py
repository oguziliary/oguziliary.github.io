from collections import OrderedDict, defaultdict

from pelican import signals  # type: ignore[import]
from pelican.utils import order_content  # type: ignore[import]


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
PLUGINS = ['render_math']

DIRECT_TEMPLATES = ['tags', 'categories', 'authors', 'archives']

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
        'categories_label': 'Categories',
        'tags_label': 'Tag',
    },
    'tr': {
        'nav_posts': 'Yazmıştı olduklarım',
        'read_more': 'Oku →',
        'from_date': 'tarihinden',
        'by_on': '{author} tarafından {date} tarihinde',
        'newer': '← Yeni',
        'older': 'Eski →',
        'categories_label': 'Kategoriler',
        'tags_label': 'Tag',
    },
}


DATE_FORMATS = {
    'en': '%B %d, %Y',      # e.g., September 21, 2025
    'tr': '%d %B %Y',       # e.g., 21 Eylül 2025
}

MONTH_NAMES = {
    'en': [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December',
    ],
    'tr': [
        'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
        'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık',
    ],
}

ENGLISH_TAGS = ["english"]

SUPERIOR_TAGS = ["english", "turkish"]

def format_date(value, lang):
    fmt = DATE_FORMATS.get(lang, '%Y-%m-%d')
    month_names = MONTH_NAMES.get(lang)

    if month_names and '%B' in fmt:
        month_name = month_names[value.month - 1]
        fmt = fmt.replace('%B', month_name)

    return value.strftime(fmt)


JINJA_FILTERS = {
    'format_date': format_date,
}


def include_translation_tags(generator):
    tags_map = defaultdict(list)

    for tag, articles in generator.tags.items():
        tags_map[tag] = list(articles)

    for translation in getattr(generator, 'translations', []):
        if getattr(translation, 'tags', None):
            for tag in translation.tags:
                if translation not in tags_map[tag]:
                    tags_map[tag].append(translation)

    for tag, articles in tags_map.items():
        tags_map[tag] = order_content(
            list(articles),
            generator.settings.get('ARTICLE_ORDER_BY', 'reversed-date'),
        )

    ordered_items = sorted(
        tags_map.items(),
        key=lambda item: item[0].name.lower(),
    )

    generator.tags = OrderedDict(ordered_items)
    generator.context['tags'] = ordered_items


signals.article_generator_finalized.connect(include_translation_tags)


THEME = "mytheme"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Article URL and save path
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{slug}-{lang}.html'

# Page URL and save path  
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

# Category URL and save path (optional)
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# Tag URL and save path (optional)
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'