from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.schemas.lead_schema import (
    ITSolutionsLead,
)

from app.core.database import (
    get_db,
)

from app.services.lead_services import (
    create_it_solution_lead,
)

router = APIRouter(
    prefix="/api/leads",
    tags=["Leads"],
)


@router.post("/it-solutions")
async def submit_it_solution_lead(
    lead: ITSolutionsLead,
    db: Session = Depends(get_db),
):

    saved_lead = create_it_solution_lead(
        db,
        lead,
    )

    return {
        "success": True,
        "message": "Lead submitted successfully",
        "lead_id": saved_lead.id,
    }