from sqlalchemy.orm import Session
from app import models, schemas

def get_vulnerabilidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vulnerabilidade).offset(skip).limit(limit).all()

def get_vulnerabilidade(db: Session, vulnerabilidade_id: int):
    return db.query(models.Vulnerabilidade).filter(models.Vulnerabilidade.id == vulnerabilidade_id).first()

def create_vulnerabilidade(db: Session, vulnerabilidade: schemas.VulnerabilidadeCreate):
    db_vuln = models.Vulnerabilidade(titulo=vulnerabilidade.titulo, descricao=vulnerabilidade.descricao)
    db.add(db_vuln)
    db.commit()
    db.refresh(db_vuln)
    return db_vuln

def update_vulnerabilidade(db: Session, vulnerabilidade_id: int, vulnerabilidade: schemas.VulnerabilidadeCreate):
    db_vuln = get_vulnerabilidade(db, vulnerabilidade_id)
    if not db_vuln:
        return None
    db_vuln.titulo = vulnerabilidade.titulo
    db_vuln.descricao = vulnerabilidade.descricao
    db.commit()
    db.refresh(db_vuln)
    return db_vuln

def delete_vulnerabilidade(db: Session, vulnerabilidade_id: int):
    db_vuln = get_vulnerabilidade(db, vulnerabilidade_id)
    if not db_vuln:
        return None
    db.delete(db_vuln)
    db.commit()
    return db_vuln
