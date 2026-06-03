from sqlalchemy.orm import Session

from app.models.it_solution_lead import (
    ITSolutionLead,
)


def create_it_solution_lead(
    db: Session,
    lead_data,
):

    lead = ITSolutionLead(
        full_name=lead_data.fullName,
        mobile=lead_data.mobile,
        email=lead_data.email,
        company=lead_data.company,
        required_service=lead_data.requiredService,
        budget=lead_data.budget,
        timeline=lead_data.timeline,
        requirement=lead_data.requirement,
    )

    db.add(lead)

    db.commit()

    db.refresh(lead)

    return lead