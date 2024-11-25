from pydantic import BaseModel
import uuid


class SRating(BaseModel):
    id: uuid.UUID
    rating: float

    class Config:
        orm_mode: True