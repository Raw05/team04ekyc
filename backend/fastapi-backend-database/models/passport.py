from pydantic import BaseModel
from datetime import datetime


class Passport(BaseModel):
    name: str
    surname: str
    gender: str
    passport_no: str
    dob: datetime
    expiry_date: datetime
