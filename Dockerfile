FROM python:3.10 AS dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim

LABEL maintainer="Stefano Pigozzi <me@steffo.eu>"
LABEL description="A customizable, multilanguage Telegram shop bot"

COPY --from=dependencies /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
ENV PYTHONUNBUFFERED=1
ENV CONFIG_PATH="/etc/greed/config.toml"
ENV DB_ENGINE="sqlite:////var/lib/greed/database.sqlite"

COPY . /usr/src/greed
WORKDIR /usr/src/greed

ENTRYPOINT ["python", "-OO"]
CMD ["core.py"]
