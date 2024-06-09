from pydantic import BaseModel

class EmailCheckResponse(BaseModel):
    is_available: bool
