import imp
from random import randint
from fastapi import APIRouter, Query, Form
from config.db import conn
from typing import Optional, Union
from sqlalchemy import select
from config.db import students, owners
from pydantic import BaseModel
import random

user  = APIRouter()


class GetOTP(BaseModel):
    contact:str
    otp:Union[str, None] = None
    fcm_token:str



@user.get("/")
async def welcome():
    return {"message":'Welcome into Easyque'}

@user.post("/api/owner/otp")
async def read_data(contact):
    otp = random.randint(100000,999999)
    try:
        return {"data":{"message":"otp created successfully.", "otp":otp, "status":True}}
    except:
        return {"data":{"message":"Something went wrong.", "status":False}}

@user.post("/api/owner/otp_verification")
async def read_data(contact = Query(default=None, alias="contact"), otp =Query(default=None, alias="otp"), fcm_token=Query(default=None, alias="fcm_token")):
    ownerRegister = owners.insert().values(contact = contact, fcm_token = fcm_token, auth_token='', active=1)
    try:
        result = conn.execute(ownerRegister)
        return {"data":{"message":"owner created successfully.", "status":True}}
    except:
        return {"data":{"message":"Something went wrong.", "status":False}}


@user.post("/api/owner/create_property")
async def create_property(data:GetOTP):
    return {"message":"done"}


@user.get("/users")
async def read_data():
    s = students.select()
    result = conn.execute(s)
    arr = []
    for i in result:
        arr.append(i)
    return {"users":arr}
