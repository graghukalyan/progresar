import time
from typing import Union
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from app.services.prospect_service import create_prospect
from app.models.prospect import Prospect

progresar_app = FastAPI()

@progresar_app.post("/prospects")
async def create_meeting_prospect(prospect: Prospect):
    attendees = create_prospect(prospect)
    return {"prospect": attendees}

@progresar_app.get("/")
def main():
    print("Welcome to Progresar! Running for 5 minutes...")
    
    start_time = time.time()
    end_time = start_time + 300  # 300 seconds = 5 minutes
    
    while time.time() < end_time:
        # Simulate some work
        time.sleep(10)
        elapsed_time = int(time.time() - start_time)
        print(f"Running... Elapsed time: {elapsed_time} seconds")
    
    return("Progresar finished running after 5 minutes.")

@progresar_app.get("/openapi.json")
def get_openapi_endpoint():
    """
    Retrieve the generated OpenAPI schema.
    """
    return JSONResponse(content=generate_openapi_schema())

def generate_openapi_schema():
    """
    Generate the OpenAPI schema for the FastAPI application.
    """
    return get_openapi(
        title="My Progresar API",
        version="1.0.0",
        description="This is my Progresar API description",
        routes=progresar_app.routes,
    )

if __name__ == "__main__":
    main()
