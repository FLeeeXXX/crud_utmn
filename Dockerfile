FROM python:3.11.9

WORKDIR /news_site

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/news_site

CMD ["sh", "-c", "python app/migrations.py && python app/news_types/seed_news_types.py && python app/news/seed_news.py && gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000"]
