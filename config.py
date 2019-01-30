import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base class for configuration items. For many of these we try and get values from environment variables with a
    fallback to hardcoded value if not defined (e.g. in dev)

    Access configuration items in the format:
    app.config['SECRET_KEY']
    """

    # used by WTForms to prevent CSRF attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-default-fallback-value'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    # Other
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
