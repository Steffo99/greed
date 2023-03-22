FROM python:3.10-alpine AS dependencies
RUN apk add --update build-base python3-dev py-pip musl-dev

WORKDIR /usr/src/greed
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --requirement requirements.txt

#############################################################################

FROM python:3.10-slim AS final

COPY --from=dependencies /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

WORKDIR /usr/src/greed
COPY . /usr/src/greed

ENTRYPOINT ["python", "-OO"]
CMD ["core.py"]

ENV PYTHONUNBUFFERED=1
ENV CONFIG_PATH="/etc/greed/config.toml"
ENV DB_ENGINE="sqlite:////var/lib/greed/database.sqlite"

LABEL org.opencontainers.image.title="greed"
LABEL org.opencontainers.image.description="A customizable, multilanguage Telegram shop bot"
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"
LABEL org.opencontainers.image.url="https://github.com/Steffo99/greed/"
LABEL org.opencontainers.image.authors="Stefano Pigozzi <me@steffo.eu>"