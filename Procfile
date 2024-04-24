release: python manage.py migrate --noinput
web: ./run_tasks.sh
worker: celery -A dtb worker -P prefork --loglevel=INFO
beat: celery -A dtb beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

