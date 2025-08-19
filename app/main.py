from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app import models, schemas
import bcrypt

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# cria tabelas
Base.metadata.create_all(bind=engine)

# templates
templates = Jinja2Templates(directory="app/templates")

# dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# rota inicial -> carrega formulário
@app.get("/", response_class=HTMLResponse)
def form_sing_up(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# rota para cadastro via JSON (API)
@app.post("/cadastro")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(user.password.encode('utf-8'), salt).decode('utf-8')

    user_db = models.User(
        name=user.name,
        email=user.email,
        fone=user.fone,
        password=pass_hash
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return {"msg": "Usuário cadastrado com sucesso!", "id": user_db.id}

