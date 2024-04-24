#!/bin/bash

python manage.py migrate
python run_polling.py
