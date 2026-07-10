FROM python:3.10-slim-bullseye
WORKDIR /app
COPY requirement.txt ./

RUN pip install --no-cache-dir awscli -r requirement.txt

COPY . /app
CMD ["python3", "app.py"]