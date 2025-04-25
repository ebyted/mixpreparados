FROM python:3.11

WORKDIR /code

# Instala dependencias del sistema, incluyendo el cliente de postgres
RUN apt-get update && apt-get install -y gcc libpq-dev postgresql-client

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# (NO hagas collectstatic aquí si usas wait-for-db)
# RUN python manage.py collectstatic --noinput

CMD ["bash", "-c", "python manage.py collectstatic --noinput && ./wait-for-db.sh db bash -c 'python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000'"]
