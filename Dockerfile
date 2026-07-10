FROM python:3.10-slim-bullseye
WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir awscli -r requirements.txt

COPY . /app
CMD ["python3", "app.py"]