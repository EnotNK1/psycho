from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# engine = create_engine(url="postgresql://postgres:1111@localhost:5432/psycho", echo=False)
engine = create_engine(url="postgresql://user:password@db:5432/dbname", echo=False)

session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
