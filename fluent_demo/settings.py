"""
Django settings for fluent_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rjm6pc^%25pt84@i-48+f2p3eya^&5(cvae9y8bl4&_wi^h86)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin', # Must come after `admin_tools`.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fluent_demo.urls'

WSGI_APPLICATION = 'fluent_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

### django ####################################################################

# Explicitly define Django defaults, so we can override and extend.

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
)

### fluent-* ##################################################################

# Common settings required by multiple `fluent-*` apps.

INSTALLED_APPS += (
    # 'django.contrib.comments',
    'django.contrib.sites',
    'django_wysiwyg',
)

DJANGO_WYSIWYG_FLAVOR = 'yui_advanced'
SITE_ID = 1

### fluent-blogs ##############################################################

INSTALLED_APPS += (
    'fluent_blogs',

    # The content plugins
    # 'fluent_contents',
    # 'fluent_contents.plugins.text',

    # Support libs
    'categories',
    'categories.editor',
    # 'django_wysiwyg',

    # Optional commenting support
    # 'django.contrib.comments',

    # Optional tagging
    'taggit',
    'taggit_autocomplete_modified',

    # Optional fluent-pages support.
    'fluent_blogs.pagetypes.blogpage',
)

### fluent-contents ###########################################################

INSTALLED_APPS += (
    'fluent_contents',

    # And optionally all plugins desired:
    'fluent_contents.plugins.code',
    # 'fluent_contents.plugins.commentsarea',
    # 'fluent_contents.plugins.disquswidgets',
    'fluent_contents.plugins.formdesignerlink',
    'fluent_contents.plugins.gist',
    'fluent_contents.plugins.googledocsviewer',
    'fluent_contents.plugins.iframe',
    'fluent_contents.plugins.markup',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.text',

    # Some plugins need extra Django applications
    # 'disqus',
    # 'django.contrib.comments',
    # 'django_wysiwyg',
    'form_designer',
)

### fluent-dashboard ##########################################################

from django.utils.translation import ugettext_lazy as _

INSTALLED_APPS += (
    'fluent_dashboard',

    # enable the admin
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin', # Must come after `admin_tools`.
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

# Optional app icons.
FLUENT_DASHBOARD_APP_ICONS = {
    # 'auth/user': 'user.png'
}

FLUENT_DASHBOARD_APP_GROUPS = (
    (_('CMS'), {
        'models': (
            'cms.*',
            'pages.*',
            'fiber.*',
        ),
        'module': 'CmsAppIconList',
        'collapsible': False,
    }),
    (_('Interactivity'), {
        'models': (
            'django.contrib.comments.*',
            'form_designer.*'
            'threadedcomments.*',
            'zinnia.*',
        ),
    }),
    (_('Administration'), {
        'models': (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            'google_analytics.*',
            'registration.*',
        ),
    }),
    (_('Applications'), {
        'models': ('*',),
        'module': 'AppList',
        'collapsible': True,
    }),
)

### Optional cache status ###

INSTALLED_APPS += (
    'dashboardmods',
)

# Example Memcache configuration:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

# Optional, example Varnish configuration:
VARNISH_MANAGEMENT_ADDRS = ('127.0.0.1:6082', )

# Enable required `request` context processor.
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

### fluent-pages ##############################################################

INSTALLED_APPS += (
    'fluent_pages',

    # Required dependencies
    'mptt',
    'parler',
    'polymorphic',
    'polymorphic_tree',

    # Optional widget pages via django-fluent-contents
    'fluent_pages.pagetypes.fluentpage',
    # 'fluent_contents',
    # 'fluent_contents.plugins.text',
    # 'django_wysiwyg',

    # Optional other CMS page types
    'fluent_pages.pagetypes.redirectnode',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'fluent-pages-templates'),
)

# FLUENT_PAGES_TEMPLATE_DIR = os.path.join(BASE_DIR, 'fluent-pages-templates')

### south #####################################################################

INSTALLED_APPS += (
    'south',
)
