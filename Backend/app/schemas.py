from pydantic import BaseModel

class VulnerabilidadeBase(BaseModel):
    titulo: str
    descricao: str
    criticidade: str

class VulnerabilidadeCreate(VulnerabilidadeBase):
    pass

class VulnerabilidadeRead(VulnerabilidadeBase):
    id: int

    class Config:
        orm_mode = True
