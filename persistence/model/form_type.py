# Importaciones
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connection.connect import Base

# Entidad modelada User
class FormType(Base):
    __tablename__ = "form_type"
    form_id = Column(Integer, primary_key=True, index=True)
    form_name = Column(String(150))

    # Relaciones
    form_type_chat = relationship("ActiveChat",back_populates="chat_form_type")