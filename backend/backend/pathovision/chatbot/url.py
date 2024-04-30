# chatbot_app/urls.py
from django.urls import path
from . import views

app_name = 'chatbot'


urlpatterns = [
    path("home", views.chatbot_page, name='chatbot_page'),
    # path('upload/', views.upload_image, name='upload'),
]




