from datetime import datetime, timedelta
import time
from typing import Annotated, Union
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session
import bcrypt
from models import User, Report
from security import hash_password, verify_password, COOKIE_NAME, oauth2_scheme, JWT_SECRET, ALGORITHM


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def get_user_by_email(self, email: str) -> User:
        return self.sess.query(User).filter(User.email == email).first()

    def get_user_by_username(self, username: str) -> User:
        return self.sess.query(User).filter(User.username == username).first()

    def create_user(self, signup: User) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except:
            print("Error")
            return False
        return True

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
        return encoded_jwt


async def get_current_user(db, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:

            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = UserRepository(db).get_user_by_username(
        username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def authenticate_user(db, username: str, password: str) -> User | bool:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

class ReportRepo:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def update_report(self, data: Report):
        try:
            self.sess.add(data)
            self.sess.commit()
        except:
            return False
        return True