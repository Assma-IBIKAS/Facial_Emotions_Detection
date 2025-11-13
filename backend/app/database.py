#* database.py — Gère la connexion à la base de données
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base 
# from dotenv import load_dotenv

# load_dotenv()

# USER = os.getenv("USER_DB")
# PASSWORD = os.getenv("PASSWORD")
# HOST = os.getenv("HOST")
# PORT = os.getenv("PORT")
# DATABASE = os.getenv("DATABASE")



USER_DB = "postgres"
PASSWORD = "0000"
HOST = "localhost"
PORT = "5432"
DATABASE = "face_detection_db"
DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

#* Crée le moteur SQLAlchemy avec l'URL depuis config.py
engine = create_engine(DATABASE_URL)

Base = declarative_base()

#* Crée une session locale pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#* Dépendance pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import declarative_base, sessionmaker
# import os
# from dotenv import load_dotenv

# load_dotenv()

# USER = os.getenv("USER_DB")
# PASSWORD = os.getenv("PASSWORD")
# HOST = os.getenv("HOST")
# PORT = os.getenv("PORT")
# DATABASE = os.getenv("DATABASE")

# # First connect to the default "postgres" database
# DEFAULT_DB_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/postgres"
# default_engine = create_engine(DEFAULT_DB_URL, isolation_level="AUTOCOMMIT")

# with default_engine.connect() as conn:
#     # Check if the target database exists
#     result = conn.execute(
#         text("SELECT 1 FROM pg_catalog.pg_database WHERE datname = :db_name"),
#         {"db_name": DATABASE},
#     )
#     if not result.fetchone():
#         conn.execute(text(f"CREATE DATABASE {DATABASE}"))
#         print(f"Database '{DATABASE}' successfully created.")
#     else:
#         print(f"Database '{DATABASE}' already exists.")

# # Now connect to your actual database
# DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
# engine = create_engine(DATABASE_URL)

# Base = declarative_base()

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def get_db():
#     """Dependency to get a database session"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()