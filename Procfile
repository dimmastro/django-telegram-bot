release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker dtb.asgi:application
worker: celery -A dtb worker -P prefork --loglevel=INFO 
beat: celery -A dtb beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
polling: python run_polling.py  # Добавляем новую строку для запуска run_polling.py - имя polling в данном случае является произвольным и может быть изменено на любое другое удобное вам.