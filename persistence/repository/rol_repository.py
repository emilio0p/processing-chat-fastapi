# Importaciones
from sqlalchemy.orm import Session
from persistence.model.rol import Rol

# Función obtener rol_id
def select_rol_name(name:str, db:Session):
    return db.query(Rol).filter(Rol.rol_name == name).first()