import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.news.router import router as news_router
from app.news_types.router import router as news_types_router
from app.news_rating.router import router as news_rating_router

app = FastAPI()
app.include_router(news_router)
app.include_router(news_types_router)
app.include_router(news_rating_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
