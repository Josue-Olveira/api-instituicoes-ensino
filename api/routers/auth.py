# Arquivo: api/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from api.core import security
from api.core.database import get_db
from api.models.base import User
from api.schemas.user import UserCreate, UserSchema
from api.schemas.token import Token
from api.core.security import get_current_user # <<< ADICIONE ESTA IMPORTAÇÃO

router = APIRouter(
    tags=["Autenticação e Usuários"]
)

@router.post("/users/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
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
    return new_user

# <<< INÍCIO DA MODIFICAÇÃO NO ENDPOINT /token >>>
@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Cria o access token
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email, "role": user.role.value}, 
        expires_delta=access_token_expires
    )
    
    # Cria o refresh token
    refresh_token = security.create_refresh_token(
        data={"sub": user.email}
    )
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "refresh_token": refresh_token
    }
# <<< FIM DA MODIFICAÇÃO >>>


# <<< ADICIONE O NOVO ENDPOINT ABAIXO >>>
@router.post("/token/refresh", response_model=Token)
def refresh_access_token(current_user: User = Depends(get_current_user)):
    """
    Gera um novo access token a partir de um refresh token válido.
    O refresh token deve ser enviado no header de autorização.
    """
    # A dependência get_current_user já valida o refresh token.
    # Se chegamos até aqui, o refresh token é válido.
    # Agora, basta criar um novo access token.
    
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    new_access_token = security.create_access_token(
        data={"sub": current_user.email, "role": current_user.role.value},
        expires_delta=access_token_expires
    )

    # Re-emitimos um novo refresh token também por segurança (opcional, mas boa prática)
    new_refresh_token = security.create_refresh_token(
        data={"sub": current_user.email}
    )
    
    return {
        "access_token": new_access_token,
        "token_type": "bearer",
        "refresh_token": new_refresh_token
    }