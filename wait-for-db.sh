#!/bin/sh

# Espera a que la base de datos esté disponible
if [ -z "$1" ]; then
  echo "Usage: $0 <host> <command>"
  exit 1
fi

HOST="$1"
shift

until pg_isready -h "$HOST" -p 5432 > /dev/null/ 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py migrate --noinput

python manage.py collectstatic --noinput

echo "Postgres is up - executing command"
exec "$@"
