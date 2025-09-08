from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a URL do banco de dados SQLite. O arquivo 'ies.db' será criado na raiz do projeto.
SQLALCHEMY_DATABASE_URL = "sqlite:///./ies.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função de dependência para obter a sessão do banco de dados em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()