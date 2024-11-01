# Dockerfile
FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev curl

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /src

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
