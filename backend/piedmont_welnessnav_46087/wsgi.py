"""
WSGI config for piedmont_welnessnav_46087 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "piedmont_welnessnav_46087.settings"
)

application = get_wsgi_application()
