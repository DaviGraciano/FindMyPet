from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    fone = Column(String, nullable=False)
    password = Column(String, nullable=False)
