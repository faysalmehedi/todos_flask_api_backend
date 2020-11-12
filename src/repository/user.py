from typing import List, Dict, Union, Optional
from src.models.user import User 

class UserRepository:

    @staticmethod
    def create_user(name: str, email: str, password: str, **kwargs) -> Optional[User]:
        existing_user = UserRepository.get_by_email(email)
        if existing_user:
            return None

        new_user = User(name, email, password, **kwargs)
        return new_user.save()

    @staticmethod
    def get_by_id(id: int) -> User:
        # TODO: implement mechanism to get user from cache
        return User.query.get(id)

    @staticmethod 
    def get_by_email(email: str) -> User:
        return User.query.filter(
            User.email == email 
        ).first()