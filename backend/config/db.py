from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

# Datos de conexión para PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL)
# Crear motor de conexión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base para los modelos
Base = declarative_base()


# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()