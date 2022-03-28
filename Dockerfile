FROM python:3.10 AS labels
LABEL maintainer="Stefano Pigozzi <me@steffo.eu>"
LABEL description="A customizable, multilanguage Telegram shop bot"

FROM labels AS dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM dependencies AS greed
COPY . /usr/src/greed
WORKDIR /usr/src/greed

FROM greed AS entry
ENTRYPOINT ["python", "-OO"]
CMD ["core.py"]

FROM entry AS environment
ENV PYTHONUNBUFFERED=1
ENV CONFIG_PATH="/etc/greed/config.toml"
ENV DB_ENGINE="sqlite:////var/lib/greed/database.sqlite"