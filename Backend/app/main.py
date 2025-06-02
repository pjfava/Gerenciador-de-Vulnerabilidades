from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ou ["*"] para testes rápidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/vulnerabilidades", response_model=list[schemas.VulnerabilidadeRead])
def read_vulnerabilidades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vulnerabilidades(db, skip=skip, limit=limit)

@app.get("/vulnerabilidades/{vulnerabilidade_id}", response_model=schemas.VulnerabilidadeRead)
def read_vulnerabilidade(vulnerabilidade_id: int, db: Session = Depends(get_db)):
    db_vuln = crud.get_vulnerabilidade(db, vulnerabilidade_id)
    if db_vuln is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vulnerabilidade não encontrada")
    return db_vuln

@app.post("/vulnerabilidades", response_model=schemas.VulnerabilidadeRead, status_code=status.HTTP_201_CREATED)
def create_vulnerabilidade(vulnerabilidade: schemas.VulnerabilidadeCreate, db: Session = Depends(get_db)):
    return crud.create_vulnerabilidade(db, vulnerabilidade)

@app.put("/vulnerabilidades/{vulnerabilidade_id}", response_model=schemas.VulnerabilidadeRead)
def update_vulnerabilidade(vulnerabilidade_id: int, vulnerabilidade: schemas.VulnerabilidadeCreate, db: Session = Depends(get_db)):
    db_vuln = crud.update_vulnerabilidade(db, vulnerabilidade_id, vulnerabilidade)
    if db_vuln is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vulnerabilidade não encontrada")
    return db_vuln

@app.delete("/vulnerabilidades/{vulnerabilidade_id}", response_model=schemas.VulnerabilidadeRead)
def delete_vulnerabilidade(vulnerabilidade_id: int, db: Session = Depends(get_db)):
    db_vuln = crud.delete_vulnerabilidade(db, vulnerabilidade_id)
    if db_vuln is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vulnerabilidade não encontrada")
    return db_vuln
