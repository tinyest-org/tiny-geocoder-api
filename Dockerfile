FROM python:3.8.6-slim

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["uvicorn", "app.server:app", "--port", "5000", "--host", "0.0.0.0"]
