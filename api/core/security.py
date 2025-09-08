from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from api.core.database import get_db
from api.models.base import User
from api.schemas.token import TokenData

# --- CONFIGURAÇÕES DE SEGURANÇA ---
SECRET_KEY = "SUA_CHAVE_SECRETA_MUITO_FORTE_E_DIFICIL_DE_ADIVINHAR"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- FUNÇÕES DE HASHING DE SENHA ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    print("\n--- DEBUG: DENTRO DE VERIFY_PASSWORD ---")
    print(f"  > Verificando a senha plana: '{plain_password}'")
    print(f"  > Contra a senha com hash: '{hashed_password}'")
    result = pwd_context.verify(plain_password, hashed_password)
    print(f"  > Resultado da verificação: {result}")
    print("------------------------------------------\n")
    return result

def get_password_hash(password: str) -> str:
    print("\n--- DEBUG: GERANDO HASH DA SENHA ---")
    print(f"  > Gerando hash para a senha: '{password}'")
    hashed = pwd_context.hash(password)
    print(f"  > Hash gerado: '{hashed}'")
    print("------------------------------------\n")
    return hashed

# ... (O resto do arquivo create_access_token e get_current_user continua igual) ...
# --- FUNÇÃO DE CRIAÇÃO DE TOKEN ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- DEPENDÊNCIA DE AUTENTICAÇÃO ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user