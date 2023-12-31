FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r src/requirements.txt

EXPOSE 5000

ENV NAME World

CMD ["python3", "src/app.py"]
