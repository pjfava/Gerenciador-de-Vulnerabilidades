from sqlalchemy.orm import Session
from . import models, schemas

def get_vulnerabilidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vulnerabilidade).offset(skip).limit(limit).all()

def get_vulnerabilidade(db: Session, vulnerabilidade_id: int):
    return db.query(models.Vulnerabilidade).filter(models.Vulnerabilidade.id == vulnerabilidade_id).first()

def create_vulnerabilidade(db: Session, vulnerabilidade: schemas.VulnerabilidadeCreate):
    db_vuln = models.Vulnerabilidade(**vulnerabilidade.dict())
    db.add(db_vuln)
    db.commit()
    db.refresh(db_vuln)
    return db_vuln

def update_vulnerabilidade(db: Session, vulnerabilidade_id: int, vulnerabilidade: schemas.VulnerabilidadeCreate):
    db_vuln = get_vulnerabilidade(db, vulnerabilidade_id)
    if db_vuln:
        for key, value in vulnerabilidade.dict().items():
            setattr(db_vuln, key, value)
        db.commit()
        db.refresh(db_vuln)
    return db_vuln

def delete_vulnerabilidade(db: Session, vulnerabilidade_id: int):
    db_vuln = get_vulnerabilidade(db, vulnerabilidade_id)
    if db_vuln:
        db.delete(db_vuln)
        db.commit()
    return db_vuln
