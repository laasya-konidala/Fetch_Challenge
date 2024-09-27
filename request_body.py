from pydantic import BaseModel
from datetime import datetime

# request body for adding points 
class AddPoints(BaseModel):
    payer: str
    points: int
    timestamp: datetime

# request body from spending points
class SpendPoints(BaseModel):
    points: int