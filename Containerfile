FROM python:3.12

WORKDIR /usr/src/greed
COPY . /usr/src/greed

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_FROZEN=1
ENV UV_NO_DEV=1
RUN uv sync --extra postgres

ENV PYTHONUNBUFFERED=1
ENV CONFIG_PATH="/etc/greed/config.toml"
ENV DB_ENGINE="sqlite:////var/lib/greed/database.sqlite"
VOLUME /etc/greed

ENTRYPOINT ["uv", "run", "python", "-OO"]
CMD ["core.py"]

LABEL org.opencontainers.image.title="Greed"
LABEL org.opencontainers.image.description="Customizable, multilanguage Telegram shop bot"
LABEL org.opencontainers.image.authors="Stefano Pigozzi <me@steffo.eu>"
LABEL org.opencontainers.image.version="0.19.1"
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"
LABEL org.opencontainers.image.url="https://forge.steffo.eu/steffo/-/packages/container/greed/latest"
LABEL org.opencontainers.image.source="https://forge.steffo.eu/steffo/greed"
