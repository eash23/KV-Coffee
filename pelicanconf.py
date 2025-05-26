AUTHOR = 'Ethan Ashley'
SITENAME = 'Kilovolt Coffee'
SITEURL = ""
SITEDESCRIPTION = "Stay Updated on KV Coffee News & Events"
THEME = 'themes/mediumfox/pelican-mediumfox'
PATH = "content"
STATIC_PATHS=['images', 'pages', 'themes/css/']
TIMEZONE = 'America/Los_Angeles'
DISPLAY_PAGES_ON_MENU = True
DEFAULT_LANG = 'en'
FAVICON = '/favicon.ico'
CSS_FILE = 'screen.css'

EXTRA_PATH_METADATA = {
    '/favicon.ico': {'path': 'favicon.ico'},  # and this
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Ethan Ashley", "https://ethanashley.com/"),
    ("Python.org", "https://www.python.org/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
