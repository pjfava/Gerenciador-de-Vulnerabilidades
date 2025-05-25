from pydantic import BaseModel, ConfigDict

# Base - atributos comuns
class VulnerabilidadeBase(BaseModel):
    titulo: str
    descricao: str | None = None

# Schema para criação de vulnerabilidades (entrada)
class VulnerabilidadeCreate(VulnerabilidadeBase):
    pass

# Schema para leitura de vulnerabilidades (saída)
class VulnerabilidadeRead(VulnerabilidadeBase):
    id: int

    # Configuração para permitir conversão de ORM para Pydantic
    model_config = ConfigDict(from_attributes=True)