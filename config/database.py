import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite"

# Leemos el dir actual, que sería database.py
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine) # Sesión de la db

Base = declarative_base() # Manejo de tablas de la db