FROM python:3.13.1-alpine3.21 AS intermediate
WORKDIR /app

RUN apk add poetry

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry export > requirements.txt

# ---

FROM python:3.13.1-alpine3.21 AS target

COPY --from=intermediate /app/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

RUN adduser -u 1000 -D user
USER user
