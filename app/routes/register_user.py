from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
import bcrypt

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

# dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

######################################### CADASTRO DE USUARIOS ##########################################################
@router.get("/", response_class=HTMLResponse)
def form_sing_up(request: Request):
    return templates.TemplateResponse("register_user.html", {"request": request})

@router.post("/cadastro")
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
