FROM python:3.11

WORKDIR /code

RUN apt-get update && apt-get install -y gcc libpq-dev postgresql-client

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
RUN chmod +x /code/wait-for-db.sh

CMD ["./wait-for-db.sh", "db", "bash", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
