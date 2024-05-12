from sqlalchemy.orm import Session
from persistence.repository.user_repository import select_all_users, insert_user
from persistence.model.user import UserAddDTO

def search_all_users(db: Session):
    return select_all_users(db)

def save_user(user: UserAddDTO, db: Session):
    return insert_user(user,db)