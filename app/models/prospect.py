from pydantic import BaseModel

class Prospect(BaseModel):
    zoomUsername: str
    password: str
    meetingDetails: str