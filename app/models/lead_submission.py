from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    JSON,
)

from datetime import datetime

from app.core.database import Base


class LeadSubmission(Base):

    __tablename__ = "lead_submissions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    service_type = Column(
        String,
        nullable=False,
    )

    enquiry_type = Column(
        String,
        nullable=False,
        default="general",
    )

    full_name = Column(
        String,
        nullable=False,
    )

    mobile = Column(
        String,
        nullable=False,
    )

    email = Column(
        String,
        nullable=False,
    )

    company = Column(
        String,
        nullable=True,
    )

    form_data = Column(
        JSON,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )