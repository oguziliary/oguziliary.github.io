from collections import OrderedDict, defaultdict

from pelican import signals  # type: ignore[import]
from pelican.utils import order_content  # type: ignore[import]


AUTHOR = 'oux'
SITENAME = 'oğuziliary'
SITENAME_TR = 'oğuziliary'
SITENAME_EN = 'oguziliary'
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
    ("github", "https://github.com/mroximut"),
    ("linkedin", "https://www.linkedin.com/in/o%C4%9Fuz-mutlu-38a129266/"),
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
        'from_date': 'from',
        'by_on': 'by {author} on {date}',
        'tags_label': 'Tag',
    },
    'tr': {
        'nav_posts': 'Yazmıştı olduklarım',
        'from_date': 'tarihinden',
        'by_on': '{author} tarafından {date} tarihinde',
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

# Utterances comments configuration
# Set this to your GitHub repository (e.g., 'username/repo-name')
# You'll also need to install the utterances app: https://github.com/apps/utterances
UTTERANCES_REPO = 'oguziliary/oguziliary.github.io'  # e.g., 'mroximut/blog' or 'mroximut/mroximut.github.io'
UTTERANCES_ISSUE_TERM = 'pathname'  # Options: 'pathname', 'url', 'title', 'og:title'
UTTERANCES_THEME = 'github-light'  # Options: 'github-light', 'github-dark', 'preferred-color-scheme', 'github-dark-orange', 'icy-dark', 'dark-blue', 'photon-dark', 'boxy-light'