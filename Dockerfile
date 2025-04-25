FROM python:3.11
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
CMD ["bash", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
