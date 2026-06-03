from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.core.database import (
    get_db,
)

from app.schemas.lead_submission_schema import (
    LeadSubmissionCreate,
)

from app.services.lead_submission_service import (
    create_lead,
)

router = APIRouter(
    prefix="/api/leads",
    tags=["Leads"],
)


@router.post("/")
async def submit_lead(
    lead: LeadSubmissionCreate,
    db: Session = Depends(get_db),
):
    print(lead)

    saved_lead = create_lead(
        db,
        lead,
    )

    return {
        "success": True,
        "leadId": saved_lead.id,
    }