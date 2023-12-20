# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from app.database.database import get_db
from app.database.users import get_user_by_username
from app.dependencies.auth import ALGORITHM, SECRET_KEY
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from app.schemas.Item import ItemCreate

from app.schemas.User import User


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


@router.post("/token")
def token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form_data.username
    password = form_data.password

    user = get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not check_password_hash(user.hashed_password, password):
        raise HTTPException(status_code=403, detail="Wrong password")

    token = jwt.encode({"sub": form_data.username},
                       SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=User)
def get_current_user(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    
    user = get_user_by_username(db, token)
    return User(id=user.id, 
                username=user.username,
                email=user.email, 
                full_name=user.full_name, 
                items=[ItemCreate(name=db_item.name, quantity=db_item.quantity) for db_item in user.items])
