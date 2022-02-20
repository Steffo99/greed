FROM python:3.10 AS labels
LABEL maintainer="Stefano Pigozzi <me@steffo.eu>"
LABEL description="A customizable, multilanguage Telegram shop bot"

FROM labels AS dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM dependencies AS greed
COPY . /usr/src/app
WORKDIR /usr/src/app

FROM greed AS entry
ENTRYPOINT ["python", "-OO"]
CMD ["core.py"]

FROM entry AS environment
ENV PYTHONUNBUFFERED=1
