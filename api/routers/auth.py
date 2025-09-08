from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from api.core import security
from api.core.database import get_db
from api.models.base import User
from api.schemas.user import UserCreate, UserSchema
from api.schemas.token import Token

router = APIRouter(
    tags=["Autenticação e Usuários"]
)

@router.post("/users/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print("\n\n--- DEBUG: RECEBIDA REQUISIÇÃO PARA CRIAR USUÁRIO ---")
    print(f"  > Dados recebidos: email='{user.email}', password='{user.password}', role='{user.role}'")

    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado"
        )
    
    hashed_password = security.get_password_hash(user.password)
    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"  > Usuário '{new_user.email}' salvo no DB com ID {new_user.id}")
    print("------------------------------------------------------\n\n")
    return new_user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("\n\n--- DEBUG: RECEBIDA REQUISIÇÃO DE LOGIN (/token) ---")
    print(f"  > Tentando login para username: '{form_data.username}' com password: '{form_data.password}'")

    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        print("  > ERRO: Usuário não encontrado no banco de dados.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    print(f"  > Usuário '{user.email}' encontrado no DB.")
    
    is_password_correct = security.verify_password(form_data.password, user.hashed_password)
    
    if not is_password_correct:
        print("  > ERRO: A verificação de senha falhou.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    print("  > SUCESSO: Senha verificada corretamente. Gerando token.")
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email, "role": user.role.value},
        expires_delta=access_token_expires
    )
    print("----------------------------------------------------\n\n")
    return {"access_token": access_token, "token_type": "bearer"}