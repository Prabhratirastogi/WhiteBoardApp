from email.mime import application
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from main.consumers import BoardConsumer 



application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        URLRouter([
                path('' , BoardConsumer)
        ])
    )
})

