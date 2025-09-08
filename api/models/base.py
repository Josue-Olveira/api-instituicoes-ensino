from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from api.core.database import Base
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    LEITOR = "leitor"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), default=UserRole.LEITOR, nullable=False)

class Mantenedora(Base):
    __tablename__ = "mantenedoras"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    
    # Relacionamento 1:N -> Uma mantenedora pode ter várias instituições
    instituicoes = relationship("Instituicao", back_populates="mantenedora", cascade="all, delete-orphan")

class Instituicao(Base):
    __tablename__ = "instituicoes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sigla = Column(String, index=True)
    mantenedora_id = Column(Integer, ForeignKey("mantenedoras.id"))
    
    # Relacionamento N:1 -> A instituição pertence a uma mantenedora
    mantenedora = relationship("Mantenedora", back_populates="instituicoes")