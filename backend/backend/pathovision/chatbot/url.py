# chatbot_app/urls.py
from django.urls import path
from . import views

app_name = 'chatbot'


urlpatterns = [
    path("upload", views.model_image, name='upload'),
    path("home", views.chatbot_page, name='chatbot_page'),
]


