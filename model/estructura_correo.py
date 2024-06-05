import os
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr

load_dotenv()


class EmailSchema(BaseModel):
    subject: str
    sender: Optional[EmailStr] = os.getenv("MAIL_USERNAME")
    recipients: List[EmailStr]
    cc: Optional[List[EmailStr]] = None
    cco: Optional[List[EmailStr]] = None
    body: str
