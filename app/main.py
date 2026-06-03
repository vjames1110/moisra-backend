from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from app.api.lead_routes import router
from app.api.lead_submission_routes import(
    router as lead_submission_router
)
from app.core.database import(
    Base,
    engine
)

from app.models.it_solution_lead import(
    ITSolutionLead,
)
from app.models.lead_submission import (
    LeadSubmission
)

app = FastAPI(
    title="MOISRA API",
    version="1.0.0",
)

Base.metadata.create_all(
    bind=engine
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://moisra.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "MOISRA API",
    }


app.include_router(router)
app.include_router(
    lead_submission_router
)