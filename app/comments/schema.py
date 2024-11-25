from pydantic import BaseModel
import uuid


class SComments(BaseModel):
    id: uuid.UUID
    news_id: uuid.UUID
    body: str

    class Config:
        orm_mode: True


class SCommentsInp(BaseModel):
    news_id: uuid.UUID
    body: str

    class Config:
        orm_mode: True
