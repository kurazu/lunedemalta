import os.path
_HERE = os.path.abspath(os.path.dirname(__file__))

AUTHOR = 'Tomasz Maćkowiak'
SITENAME = 'Lune de Malta'
SITEURL = ""

THEME = os.path.join(_HERE, "themes", "chunk")
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
SITESUBTITLE = 'Nieoficjalna strona Wspólnoty Mieszkaniowej Lune de Malta w Poznaniu'
FOOTER_TEXT = 'CC'
SINGLE_AUTHOR = True
MINT = False
DISPLAY_CATEGORIES_ON_MENU = False

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
