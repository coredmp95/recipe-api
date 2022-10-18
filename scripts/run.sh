#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py colllectstatic --noinput
python manage.py migrate

uswgi --socket :9000  --workers 4 --master --enable-thread --module app.wsgi
