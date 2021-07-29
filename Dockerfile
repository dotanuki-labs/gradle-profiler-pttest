FROM python:3.9-slim-buster

WORKDIR /tmp

RUN python -m pip install --upgrade pip && pip install poetry

COPY . .

RUN poetry build && find ./dist -name "*.tar.gz" -exec pip install {} \;

ENTRYPOINT ["gradle-profiler-pttest"]
