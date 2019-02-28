FROM python:3.4-alpine
ADD code/ /code
WORKDIR /code
RUN apk add --no-cache gcc mailcap python3-dev build-base linux-headers pcre-dev postgresql-dev libffi-dev libressl-dev
RUN pip install -r requirements.txt
CMD ["python", "app.py"]