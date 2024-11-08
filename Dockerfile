FROM python:3.11.9

RUN mkdir /news_site

WORKDIR /news_site

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000