FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7
COPY code/ /app
WORKDIR /app
RUN apk add --no-cache gcc mailcap python3-dev build-base linux-headers pcre-dev postgresql-dev libffi-dev libressl-dev
RUN pip install -r requirements.txt