from sqlalchemy.orm import Session
from persistence.model.user import User, UserAddDTO

def select_all_users(db: Session):
    return db.query(User).all()

def insert_user(user: UserAddDTO, db: Session):
    db_user = User(username=user.username, email=user.email, password=user.password, phone=user.phone, rol=user.rol)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user