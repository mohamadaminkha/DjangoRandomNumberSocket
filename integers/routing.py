from django.urls import path
from .consumers import WConsumer

ws_urlpatterns = [
    path('ws/some_url/',WConsumer.as_asgi())
]