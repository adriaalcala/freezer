FROM python:3.9-slim

RUN pip install --no-cache-dir pipenv==2018.11.26

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy && rm -rf ~/.cache/

ARG CACHEBUST=1
RUN echo "$CACHEBUST"


ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 app:app

COPY . ./
