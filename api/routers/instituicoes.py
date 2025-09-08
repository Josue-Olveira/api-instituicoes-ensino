from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from api.core.database import get_db
from api.models.base import Instituicao, Mantenedora, User, UserRole
from api.schemas.instituicao import InstituicaoSchema, InstituicaoCreate, MantenedoraSchema, MantenedoraCreate
from api.core.security import get_current_user

router = APIRouter(
    prefix="/api",
    tags=["Instituições e Mantenedoras"]
)

# --- Endpoints para Mantenedoras ---

@router.post("/mantenedoras/", response_model=MantenedoraSchema, status_code=status.HTTP_201_CREATED)
def create_mantenedora(
    mantenedora: MantenedoraCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: permissão de administrador necessária."
        )

    db_mantenedora = db.query(Mantenedora).filter(Mantenedora.nome == mantenedora.nome).first()
    if db_mantenedora:
        raise HTTPException(status_code=400, detail="Mantenedora com este nome já existe")
    
    nova_mantenedora = Mantenedora(nome=mantenedora.nome)
    db.add(nova_mantenedora)
    db.commit()
    db.refresh(nova_mantenedora)
    return nova_mantenedora

@router.get("/mantenedoras/", response_model=List[MantenedoraSchema])
def read_mantenedoras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mantenedoras = db.query(Mantenedora).offset(skip).limit(limit).all()
    return mantenedoras

# --- Endpoints para Instituições ---

@router.post("/instituicoes/", response_model=InstituicaoSchema, status_code=status.HTTP_201_CREATED)
# <<< A CORREÇÃO ESTÁ NA LINHA ABAIXO, GARANTINDO O NOME CORRETO
def create_instituicao(instituicao: InstituicaoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: permissão de administrador necessária."
        )

    db_mantenedora = db.query(Mantenedora).filter(Mantenedora.id == instituicao.mantenedora_id).first()
    if not db_mantenedora:
        raise HTTPException(status_code=404, detail="Mantenedora não encontrada")
        
    nova_instituicao = Instituicao(**instituicao.dict())
    db.add(nova_instituicao)
    db.commit()
    db.refresh(nova_instituicao)
    return nova_instituicao

@router.get("/instituicoes/", response_model=List[InstituicaoSchema])
def read_instituicoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    instituicoes = db.query(Instituicao).offset(skip).limit(limit).all()
    return instituicoes