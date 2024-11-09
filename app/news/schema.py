from pydantic import BaseModel


class SNews(BaseModel):
    title: str
    subtitle: str
    body: str

    class Config:
        orm_mode: True
