FROM python:3.11

# Set workdir
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install pip dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# Collect static at build-time (Django must be ready for production)
RUN python manage.py collectstatic --noinput

# Entrypoint for migrations and running server
CMD ["bash", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]