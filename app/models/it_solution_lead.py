from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)

from datetime import datetime

from app.core.database import Base


class ITSolutionLead(Base):

    __tablename__ = (
        "it_solution_leads"
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
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

    required_service = Column(
        String,
        nullable=False,
    )

    budget = Column(
        String,
        nullable=True,
    )

    timeline = Column(
        String,
        nullable=True,
    )

    requirement = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )