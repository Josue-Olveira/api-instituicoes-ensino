from pydantic import BaseModel
from typing import Optional # <<< IMPORTAÇÃO NECESSÁRIA

# ==================================
# Schemas para a entidade Mantenedora
# ==================================
class MantenedoraBase(BaseModel):
    nome: str

class MantenedoraCreate(MantenedoraBase):
    pass

class MantenedoraSchema(MantenedoraBase):
    id: int

    class Config:
        from_attributes = True

# ===================================
# Schemas para a entidade Instituicao
# ===================================
class InstituicaoBase(BaseModel):
    nome: str
    # <<< A CORREÇÃO ESTÁ AQUI
    sigla: Optional[str] = None # Tornamos a sigla opcional

class InstituicaoCreate(InstituicaoBase):
    mantenedora_id: int

class InstituicaoSchema(InstituicaoBase):
    id: int
    mantenedora: MantenedoraSchema

    class Config:
        from_attributes = True