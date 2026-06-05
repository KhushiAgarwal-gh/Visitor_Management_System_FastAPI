from fastapi import FastAPI, Query,HTTPException
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import random
import bcrypt
import re
from datetime import datetime, timedelta
from jose import jwt
from zoneinfo import ZoneInfo
from sqlalchemy import and_
import cv2
#import shutil
#import os
from fastapi import UploadFile,File,Form
from sqlalchemy import func

app = FastAPI()

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()



class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String, unique=True)

    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    phone_number = Column(String)
    address = Column(String)
    authority = Column(String)
    id_type = Column(String)
    id_number = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    check_in = Column(DateTime, nullable=True)
    check_out = Column(DateTime, nullable=True)





class SignupModel(BaseModel):

    name: str
    email: str
    password: str

    @validator("email")
    def email_validate(cls, v):
        pattern = r"^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com|outlook\.com)$"
        if not re.match(pattern, v):
            raise ValueError("Invalid email")
        return v

    @validator("password")
    def password_validate(cls, v):
        if len(v) < 8:
            raise ValueError("Min 8 chars required")
        if not re.search(r"[A-Za-z]", v):
            raise ValueError("Need letter")
        if not re.search(r"[0-9]", v):
            raise ValueError("Need number")
        if not re.search(r"[@$!%*?&]", v):
            raise ValueError("Need special char")
        return v




class CreateUser(BaseModel):
    

    name:str=Form(...)
    email: str=Form(...)
    phone_number: str=Form(...)
    address: str=Form(...)
    authority: str=Form(...)
    id_type: str=Form(...)
    id_number: str=Form(...)
    
    

    @validator("phone_number")
    def phone_validate(cls, v):
        if not re.match(r'^[6-9][0-9]{9}$', v):
            raise ValueError("Invalid phone number")
        return v

    @validator("authority")
    def authority_validate(cls, v):
        allowed = ["intern", "employee", "manager"]
        if v.lower() not in allowed:
            raise ValueError("Not allowed")
        return v

    @validator("id_number")
    def id_validate(cls, v, values):

        id_type = values.get("id_type")

        if not id_type:
            raise ValueError("ID type required")

        if id_type.lower() == "aadhaar":
            if not re.match(r'^[2-9]{1}[0-9]{11}$', v):
                raise ValueError("Invalid Aadhaar number")

        elif id_type.lower() == "pan":
            if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', v):
                raise ValueError("Invalid PAN number")

        elif id_type.lower() == "driving_licence":
            if not re.match(r'^[A-Z]{2}[0-9]{2}[0-9]{11}$', v):
                raise ValueError("Invalid Driving Licence number")

        else:
            raise ValueError("Invalid ID type")

        return v
    
class Visitor(Base):

    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True)
    visitor_id = Column(String, unique=True)

    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

    authority = Column(String)
    id_type = Column(String)
    id_number = Column(String)
    photo = Column(String)
    
    check_in = Column(DateTime, nullable=True)
    check_out = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)




class LoginModel(BaseModel):
    email_or_user_id: str
    password: str

class LogoutModel(BaseModel):

    email_or_user_id: str
    password: str

class ActionModel(BaseModel):
    email_or_user_id: str




SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def create_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=30)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def generate_user_id():
    return f"USR{random.randint(1000,9999)}"



@app.post("/signup")
def signup(name:str=Form(...),email:str=Form(...),password:str=Form(...)):

    db = SessionLocal()

    if db.query(User).filter(User.email == email).first():
        return {"message": "Email already exists"}

    uid = generate_user_id()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = User(
        user_id=uid,
        name=name,
        email=email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()

    return {
        
    "message": "Signup successful",
    "user_id": uid,
    "name": name,
    "email": email
}

@app.post("/login")
def login(email_or_user_id: str = Form(...),
    password: str = Form(...) ):

    db = SessionLocal()

    db_user = db.query(User).filter(
        (User.email == email_or_user_id) |
        (User.user_id == email_or_user_id)
    ).first()

    if not db_user:
        return {"message": "Invalid credentials"}

    if not bcrypt.checkpw(password.encode(), db_user.password.encode()):
        return {"message": "Invalid credentials"}

    db_user.last_login = datetime.now(ZoneInfo("Asia/Kolkata"))
    db.commit()

    return {
        "message": "Login successful",
        "token": create_token({"sub": db_user.email}),
        "user_id": db_user.user_id,
        "name": db_user.name,
        "email": db_user.email
    }


@app.post("/create-visitor")
async def create_visitor(
    name: str = Form(...), email: str = Form(...), phone_number: str = Form(...), address: str = Form(...), authority: str = Form(...), id_type: str = Form(...), id_number: str = Form(...),
    photo: UploadFile = File(...)
):

    db = SessionLocal()

    if authority.lower() not in ["intern", "employee", "manager"]:

        return {

            "message": "Not allowed to meet",

            "meeting_status": "Denied"
        }

    visitor_id = f"VIS{random.randint(1000,9999)}"
    
   # if not os.path.exists("photos"): os.makedirs("photos")

    #file_path = f"photos/{visitor_id}.jpg"

    #with open(file_path, "wb") as buffer:
       # shutil.copyfileobj(photo.file, buffer)

    #img = cv2.imread(file_path)

    visitor = Visitor(

        visitor_id=visitor_id,

        name=name,

        email=email,

        phone_number=phone_number,

        address=address,

        authority=authority,

        id_type=id_type,

        id_number=id_number,

        #photo=file_path
    )

    db.add(visitor)

    db.commit()

    return {

        "message": "Visitor created successfully",

        "visitor_id": visitor.visitor_id,

        "meeting_status": "Allowed",

        "name": visitor.name,

        "email": visitor.email,

        "authority": visitor.authority,

        #"photo": visitor.photo
    }




@app.put("/visitor/checkin")
def checkin(data: ActionModel):

    db = SessionLocal()

    visitor = db.query(Visitor).filter(
        (Visitor.email == data.email_or_user_id) |
        (Visitor.visitor_id == data.email_or_user_id)
    ).first()

    if not visitor:
        return {
            "message": "Visitor not found"
        }

    

    visitor.check_in = datetime.now(ZoneInfo("Asia/Kolkata"))

    db.commit()

    return {

        "message": "Check-in successful",


        "visitor_id": visitor.visitor_id,

        "name": visitor.name,

        "email": visitor.email,

        "phone_number": visitor.phone_number,

        "address": visitor.address,

        "authority": visitor.authority,

        "id_type": visitor.id_type,

        "id_number": visitor.id_number,

        #"photo":visitor.photo,

        "check_in_time": visitor.check_in
    }



@app.get("/visitors")
def get_visitors(
    name: str = Query(None),
    email: str = Query(None),
    authority: str = Query(None),
    visitor_id: str = Query(None),
    check_in_date: str = Query(None),
    time_range: str = Query(None)
):

    db = SessionLocal()
    query = db.query(Visitor)

    if time_range and time_range.strip():
        try:
            times = time_range.split("-")
            if len(times) != 2:
                raise ValueError

            start_time_str, end_time_str = times[0].strip(), times[1].strip()

            t_start = datetime.strptime(start_time_str, "%H:%M:%S").time()
            t_end = datetime.strptime(end_time_str, "%H:%M:%S").time()

            query = query.filter(
                Visitor.check_in.isnot(None),
                func.time(Visitor.check_in).between(t_start, t_end)
            )

        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Incorrect time_range format. Use HH:MM:SS-HH:MM:SS"
            )

    if name:
        query = query.filter(Visitor.name == name)

    if email:
        query = query.filter(Visitor.email == email)

    if authority:
        query = query.filter(Visitor.authority == authority)

    if visitor_id:
        query = query.filter(Visitor.visitor_id == visitor_id)

    if check_in_date:
        check_date = datetime.fromisoformat(check_in_date).date()
        query = query.filter(
            Visitor.check_in.isnot(None),
            Visitor.check_in.between(
                datetime.combine(check_date, datetime.min.time()),
                datetime.combine(check_date, datetime.max.time())
            )
        )

    visitors = query.all()

    return {
        "total_visitors": len(visitors),
        "filters_applied": {
            "name": name,
            "email": email,
            "authority": authority,
            "visitor_id": visitor_id,
            "check_in_date": check_in_date,
            "time_range": time_range
        },
        "data": [
            {
                "visitor_id": v.visitor_id,
                "name": v.name,
                "email": v.email,
                "phone_number": v.phone_number,
                "authority": v.authority,
                "check_in_time": v.check_in,
                "check_out_time": v.check_out,
                "check_in_date": v.check_in.date() if v.check_in else None
            }
            for v in visitors
        ]
    }

@app.put("/visitor/checkout")
def checkout(data: ActionModel):

    db = SessionLocal()

    visitor = db.query(Visitor).filter(
        (Visitor.email == data.email_or_user_id) |
        (Visitor.visitor_id == data.email_or_user_id)
    ).first()

    if not visitor:
        return {
            "message": "Visitor not found"
        }

    visitor.check_out = datetime.now(ZoneInfo("Asia/Kolkata"))

    db.commit()

    return {

        "message": "Check-out successful",

        "visitor_id": visitor.visitor_id,

        #"photo":visitor.photo,

        "check_out_time": visitor.check_out
    }





@app.delete("/delete-user")
def delete_user(data: ActionModel):

    db = SessionLocal()

    user = db.query(User).filter(
        (User.email == data.email_or_user_id) |
        (User.user_id == data.email_or_user_id)
    ).first()

    if not user:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}


@app.post("/logout")
def logout(data: LogoutModel):

    db = SessionLocal()

    user = db.query(User).filter(
        (User.email == data.email_or_user_id) |
        (User.user_id == data.email_or_user_id)
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    is_valid_password = bcrypt.checkpw(
        data.password.encode('utf-8'),
        user.password.encode('utf-8')
    )

    if not is_valid_password:
        return {
            "message": "Invalid password"
        }

    return {
        "message": "Logout successful",
        "user_id": user.user_id,
        "email": user.email
    }