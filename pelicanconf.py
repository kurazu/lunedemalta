import os.path
import hashlib
_HERE = os.path.abspath(os.path.dirname(__file__))

AUTHOR = 'Tomasz Maćkowiak'
EMAIL = 'kurazu@kurazu.net'
EMAIL_SHA256 = hashlib.sha256(EMAIL.encode('utf-8')).hexdigest()

SITENAME = 'Lune de Malta'
SITEURL = ""

THEME = os.path.join(_HERE, "themes", "genus")
SITETITLE = 'Lune de Malta'
COPYRIGHT_YEAR = 2025
SITESUBTITLE = 'Nieoficjalna strona Wspólnoty Mieszkaniowej Lune de Malta w Poznaniu'
GRAVATAR_IMAGE = f'https://www.gravatar.com/avatar/{EMAIL_SHA256}?s=200&d=identicon&r=g'
PATH = "content"

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    # ("Grupa FB", "https://www.facebook.com/groups/780238453500371"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# --- Favicon and manifest static files ---
STATIC_PATHS = [
    'images',
    'extra/apple-touch-icon.png',
    'extra/favicon-32x32.png',
    'extra/favicon-16x16.png',
    'extra/favicon.ico',
    'extra/site.webmanifest',
]
EXTRA_PATH_METADATA = {
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
}
