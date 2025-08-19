from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from .routes import register_user

app = FastAPI()

# monta arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# cria tabelas
Base.metadata.create_all(bind=engine)

# inclui as rotas de usuário
app.include_router(register_user.router, tags=["Usuários"])

