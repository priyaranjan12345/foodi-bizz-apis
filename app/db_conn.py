from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'priyaranjan'
password = 'password'

database_url = f'mysql+pymysql://{user}:{password}@localhost/foodibizz'

engine = create_engine(database_url)

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()