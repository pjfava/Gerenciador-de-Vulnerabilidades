from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Vulnerabilidade(Base):
    __tablename__ = "vulnerabilidades"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
