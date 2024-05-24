# Importaciones
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from connection.connect import Base
from persistence.model.active_chat import ActiveChat

# Entidad modelada User
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(40))
    password = Column(String(64))
    phone = Column(String(20))
    rol_id = Column(Integer, ForeignKey("roles.rol_id"))

    # Relaciones
    user_rol = relationship("Rol", back_populates="rol_users")
    user_client_chat = relationship("ActiveChat",foreign_keys="ActiveChat.client_id", back_populates="chat_user_client", cascade="all, delete-orphan")
    user_admin_chat = relationship("ActiveChat",foreign_keys="ActiveChat.admin_id", back_populates="chat_user_admin", cascade="all, delete-orphan")