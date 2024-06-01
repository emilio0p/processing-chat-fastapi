# Importaciones
from connection.connect import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


# TODO BORRAR
# message_id INT AUTO_INCREMENT PRIMARY KEY,
#   chat_id INT,
#   user_id INT,
#   content TEXT,
#   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#   FOREIGN KEY (chat_id) REFERENCES active_chats(chat_id),
#   FOREIGN KEY (user_id) REFERENCES users(user_id),

#Modelamos la Entidad
class Message(Base):
    #Indicamos el nombre de la tabla en la bbdd
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("active_chats.chat_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    content = Column(String)
    timestamp = Column(DateTime, default=func.now(), nullable=False)
    #El atributo rol_users es instancia de la clase User y está relacionado
    #con el atributo user_rol de la clase Rol
    message_chat = relationship("ActiveChat", back_populates="chat_message")
    message_user = relationship("User", back_populates="user_message")
