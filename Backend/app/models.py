from sqlalchemy import Column, Integer, String
from .database import Base

class Vulnerabilidade(Base):
    __tablename__ = "vulnerabilidades"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=False)
    criticidade = Column(String(50), nullable=False)
