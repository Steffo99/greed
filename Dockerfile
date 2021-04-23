FROM python:3.9-slim-buster
LABEL maintainer="ste.pigozzi@gmail.com" \
      description="A customizable, multilanguage Telegram shop bot"
COPY . /app
WORKDIR "./app"
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3", "-OO", "core.py"]
