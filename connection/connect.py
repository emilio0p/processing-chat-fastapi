# Importaciones
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargamos el .env
load_dotenv()

# String de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

# Creamos la conexión
engine = create_engine(DATABASE_URL)

# Instanciamos fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define la base declarativa para las entidades
Base = declarative_base()

# Sesiones
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
