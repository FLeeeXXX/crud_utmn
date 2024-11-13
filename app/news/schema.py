from pydantic import BaseModel
import uuid


class SNews(BaseModel):
    id: uuid.UUID
    title: str
    subtitle: str
    body: str

    class Config:
        orm_mode: True


class SNewsView(BaseModel):
    title: str
    subtitle: str
    body: str

    class Config:
        orm_mode: True