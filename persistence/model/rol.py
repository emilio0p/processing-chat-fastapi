# Importaciones
from connection.connect import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

#Modelamos la Entidad
class Rol(Base):
    #Indicamos el nombre de la tabla en la bbdd
    __tablename__ = 'roles'
    rol_id = Column(Integer, primary_key=True, index=True)
    rol_name = Column(String(20), unique=True, nullable=False)
    #El atributo rol_users es instancia de la clase User y está relacionado
    #con el atributo user_rol de la clase Rol
    rol_users = relationship("User", back_populates="user_rol")