#!/bin/bash

echo '0'
gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker dtb.asgi:application
echo '1'
python run_polling.py
echo '2'
