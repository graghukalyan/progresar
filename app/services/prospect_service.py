from app.models.prospect import Prospect
from app.utils.api_client import get_meeting_attendees

def create_prospect(prospect: Prospect):
    """
    Create a meeting prospect.
    This function simulates creating a meeting prospect by printing a message.
    Args:
        prospect (Prospect): The prospect to create.
    """
    validate_request(prospect)
    
    print(f"Gathering data for meeting prospects for meeting: {prospect.meetingDetails}")
    attendees = get_meeting_attendees(prospect.meetingDetails)
    print(f"The list of meeting attendees :{attendees}")
    return attendees

def validate_request(prospect: Prospect):
    """
    Validate the request.
    """
    
    if not prospect.zoomUsername or not prospect.password:
        raise ValueError("Invalid request as some credentials are missing.")
    
    if not prospect.meetingDetails:
        raise ValueError("Invalid request as meeting details are missing.")
    