# Importaciones
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connection.connect import Base

# Entidad modelada User
class ChatStatus(Base):
    __tablename__ = "chat_status"
    status_id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String(50))

    # Relaciones
    chat_status_chat = relationship("ActiveChat",back_populates="chat_chat_status")