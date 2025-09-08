from pydantic import BaseModel
from typing import Optional

# Schemas para a entidade Mantenedora
class MantenedoraBase(BaseModel):
    nome: str

class MantenedoraCreate(MantenedoraBase):
    pass

class MantenedoraSchema(MantenedoraBase):
    id: int
    class Config:
        from_attributes = True

# Schemas para a entidade Instituicao
class InstituicaoBase(BaseModel):
    nome: str
    sigla: Optional[str] = None
    
    # <<< INÍCIO DA MODIFICAÇÃO >>>
    municipio: Optional[str] = None
    uf: Optional[str] = None
    # <<< FIM DA MODIFICAÇÃO >>>

class InstituicaoCreate(InstituicaoBase):
    mantenedora_id: int

class InstituicaoSchema(InstituicaoBase):
    id: int
    mantenedora: MantenedoraSchema
    class Config:
        from_attributes = True