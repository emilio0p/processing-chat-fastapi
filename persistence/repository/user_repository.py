# Importaciones
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError 
from persistence.model.user import User
from persistence.model.user_dto import UserAddDTO

# Función seleccionar todos los usuarios
def select_all_users(db: Session):
    return db.query(User).all()

# Función insertar un usuario
def insert_user(user: UserAddDTO, rol:int, db: Session):
    db_user = User(username=user.username, email=user.email, password=user.password, phone=user.phone, rol_id=rol)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Función seleccionar usuario por id
def select_user_by_id(user_id: int, db: Session):
   return db.query(User).filter(User.user_id==user_id).first()

# Función seleccionar usuario por email
def select_user_by_email(user_email: str, db: Session):
    return db.query(User).filter(User.email==user_email).first()

# Función editar usuario
def update_user(db_user: User, user: UserAddDTO, db: Session):
   db_user.username=user.username
   db_user.email=user.email
   db_user.phone=user.phone
   db_user.password = user.password
   db.commit()
   db.refresh(db_user)
   return db_user

# Función eliminar usuario
def delete_user(db_user: User, db: Session):
    db.delete(db_user)
    db.commit()

