from fastapi import FastAPI
from api.core.database import engine, Base
# --- Linhas para Alterar/Adicionar ---
from api.routers.instituicoes import router as instituicoes_router
from api.routers.auth import router as auth_router # Adicione esta linha

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Instituições de Ensino",
    description="API RESTful para consulta de dados de Instituições de Ensino Superior do Brasil.",
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seu-email@exemplo.com",
    },
)

# Inclui os routers na aplicação principal
app.include_router(auth_router) # Adicione esta linha
app.include_router(instituicoes_router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Instituições de Ensino!"}