# Importaciones
from sqlalchemy.orm import Session
from persistence.model.form_type import FormType

# Función obtener rol_id
def select_form_by_name(name:str, db:Session):
    return db.query(FormType).filter(FormType.form_name == name).first()

def select_form_by_id(id:int, db:Session):
    return db.query(FormType).filter(FormType.form_id == id).first()