from pydantic import BaseModel
from datetime import datetime


class PanCard(BaseModel):
    name: str
    dob: datetime
    father_name: str
    pan_no: str
