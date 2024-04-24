"""
WSGI config for dtb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from run_polling import run_polling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtb.settings')

run_polling()

application = get_wsgi_application()
