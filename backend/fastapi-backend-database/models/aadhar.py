from pydantic import BaseModel
from datetime import datetime


class AadharCard(BaseModel):
    name: str
    dob: str
    gender: str
    aadhar_no: str
