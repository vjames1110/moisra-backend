from sqlalchemy.orm import Session

from app.models.lead_submission import (
    LeadSubmission,
)


def create_lead(
    db: Session,
    lead_data,
):

    lead = LeadSubmission(
        service_type=lead_data.serviceType,
        enquiry_type=lead_data.enquiryType,

        full_name=lead_data.fullName,
        mobile=lead_data.mobile,
        email=lead_data.email,
        company=lead_data.company,

        form_data=lead_data.formData,
    )

    db.add(lead)

    db.commit()

    db.refresh(lead)

    return lead