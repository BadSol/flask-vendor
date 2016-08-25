import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'vendor/SECRETS.json')) as data_file:
    secrets = json.load(data_file)


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = secrets["secret_key"]

    DATABASE_URI = 'postgresql://{}:{}@localhost/{}'.format(secrets["db_user"],
                                                            secrets["db_password"],
                                                            secrets["db_name"])


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False