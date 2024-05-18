# Importaciones
from sqlalchemy.orm import Session
from persistence.model.user import User, UserAddDTO

# Función seleccionar todos los usuarios
def select_all_users(db: Session):
    return db.query(User).all()

# Función insertar un usuario
def insert_user(user: UserAddDTO, db: Session):
    db_user = User(username=user.username, email=user.email, password=user.password, phone=user.phone, rol=user.rol)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Función seleccionar usuario por id
def select_user_by_id(user_id: int, db: Session):
   return db.query(User).filter(User.user_id==user_id).first()

# Función editar usuario
def update_user(db_user: User, user: UserAddDTO, db: Session):
   db_user.username=user.username
   db_user.email=user.email
   db_user.phone=user.phone
   db_user.password = user.password
   db.commit()
   db.refresh(db_user)
   return db_user

