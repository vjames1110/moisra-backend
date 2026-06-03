from pydantic import (
    BaseModel,
    EmailStr,
)

from typing import (
    Optional,
    Dict,
    Any,
)


class LeadSubmissionCreate(
    BaseModel
):

    serviceType: str

    enquiryType: str = "general"

    fullName: str

    mobile: str

    email: EmailStr

    company: Optional[str] = None

    formData: Dict[str, Any]