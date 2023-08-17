"""
ASGI config for whiteboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whiteboard.settings')

# application = get_asgi_application()
import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from main.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_channels.settings')

application = get_asgi_application()

ws_patterns = [
path('ws/test/', BoardConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})