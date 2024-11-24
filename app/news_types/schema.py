from pydantic import BaseModel
import uuid


class SNewsTypes(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        orm_mode: True


class SNewsTypesView(BaseModel):
    name: str

    class Config:
        orm_mode: True
