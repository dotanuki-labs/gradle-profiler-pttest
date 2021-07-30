FROM python:3.9-slim-buster as builder

RUN python -m pip install --upgrade pip && pip install poetry

COPY . .

RUN poetry build && find ./dist -name "*.tar.gz" -exec mv {} /tmp/gpp.tar.gz  \;


FROM python:3.9-slim-buster

COPY --from=builder /tmp/gpp.tar.gz .

RUN python -m pip install --upgrade --no-cache-dir pip && \
	pip install --no-cache-dir gpp.tar.gz && \
	rm gpp.tar.gz

ENTRYPOINT ["gradle-profiler-pttest"]
