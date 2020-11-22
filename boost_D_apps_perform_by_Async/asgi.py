"""
ASGI config for boost_D_apps_perform_by_Async project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boost_D_apps_perform_by_Async.settings')

application = get_asgi_application()
