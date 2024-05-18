# Importaciones
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connection.connect import Base
from pydantic import BaseModel

# Entidad modelada User
class Form(Base):
    __tablename__ = "form_type"
    form_id = Column(Integer, primary_key=True, index=True)
    form_name = Column(String(100))

