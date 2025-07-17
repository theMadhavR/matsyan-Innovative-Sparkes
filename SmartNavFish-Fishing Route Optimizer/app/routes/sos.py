from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth import get_current_user
from app.models.user import User
from app.config import settings
from twilio.rest import Client
from pydantic import BaseModel

router = APIRouter()

class SOSRequest(BaseModel):
    latitude: float
    longitude: float
    message: str = None

@router.post("/sos")
def send_sos(
    sos_data: SOSRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #Twilio Client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    #emergency msg
    message_body = f"""
    EMERGENCY ALERT FROM SMARTNAVFISH:
    User: {current_user.username} ({current_user.phone_number})
    Vessel: {current_user.vessel_name or 'Unknown'}
    
    Location: {sos_data.latitude}, {sos_data.longitude}
    {sos_data.message or 'No additional message provided.'}
    
    Sent at: {datetime.datetime.utcnow()}
    """
    
    try:
        # Send SMS to emergency contacts
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=current_user.phone_number  # In real implementation, this would be emergency contacts
        )
        
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send SOS: {str(e)}")
