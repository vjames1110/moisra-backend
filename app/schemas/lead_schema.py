from pydantic import BaseModel, EmailStr
from typing import Optional


class ITSolutionsLead(BaseModel):
    fullName: str
    mobile: str
    email: EmailStr

    company: Optional[str] = None

    requiredService: str

    budget: Optional[str] = None

    timeline: Optional[str] = None

    requirement: str