from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from vendor.config import secrets


engine = create_engine('postgresql://{}:{}@localhost/{}'.format(
    secrets["db_user"],
    secrets["db_password"],
    secrets["db_name"]),
    convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    # import vendor.models
    print 'Initiating database!'
    Base.metadata.create_all(bind=engine)