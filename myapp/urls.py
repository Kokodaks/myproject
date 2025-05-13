from django.urls import path
from .views import hello_api
from .views import receive_post

urlpatterns = [
    path('hello/', hello_api),
    path('post/', receive_post)
]