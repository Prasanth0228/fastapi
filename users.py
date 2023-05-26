from fastapi import APIRouter, Depends, HTTPException
from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session
#import crud to give access to the operations that we defined
from crud import useroper

from database import SessionLocal
from models import usermodel
from models.usermodel import User,UserJson
from database import engine
#from schemas import userschema
#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/tmpusers",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)



#create the database tables on app startup or reload
usermodel.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
#define endpoint
@router.post("/adduser")
async def create_user(first_name:str, password:str, email_id:str, db:Session = Depends(get_db)):
    user = useroper.create_user(db=db, first_name=first_name, password=password, email_id=email_id)
##return object created
    return {"user": user}
'''
#define endpoint
@router.post("/adduser")
async def create_user(user: usermodel.UserCreate, db:Session = Depends(get_db)):

    #user = useroper.create_user(db=db, first_name=user.first_name, password=user.password, email_id=user.email_id)
    user = useroper.create_user(db=db, user=user)
##return object created
    return {"user": user}

@router.get("/listusers")
async  def list_users(db:Session = Depends(get_db)):
    """
    Fetch a list of all Friend object
    Returns a list of objects
    """

    return useroper.userlist(db=db)
    #return users_list

@router.get("/fetchusers")
async  def fetchusers(db:Session = Depends(get_db)):
    """
    Fetch a list of all Friend object
    Returns a list of objects
    """

    users_list = useroper.list_friends(db=db)
    return users_list