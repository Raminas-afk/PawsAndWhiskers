"""
WSGI config for pawsandwhiskers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawsandwhiskers.settings')

application = get_wsgi_application()

# Use WhiteNoise for serving static file
application = WhiteNoise(application)
