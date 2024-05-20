# Importaciones
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from connection.connect import Base
from persistence.model.form_type import FormType

# Entidad modelada User
class ActiveChat(Base):
    __tablename__ = "active_chats"
    chat_id = Column(Integer, primary_key=True, index=True)
    chat_name = Column(String)
    client_id = Column(Integer, ForeignKey("users.user_id"))
    admin_id = Column(Integer, ForeignKey("users.user_id"))
    form_id = Column(Integer, ForeignKey("form_type.form_id"))

    # Relaciones
    chat_user_client = relationship("User",foreign_keys=[client_id], back_populates="user_client_chat")
    chat_user_admin = relationship("User",foreign_keys=[admin_id], back_populates="user_admin_chat")
    chat_form_type = relationship("FormType", back_populates="form_type_chat")