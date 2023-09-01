# new_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send-message/<int:user_id>/', views.send_message_view, name='send_message'),
    # Other URL patterns for your app
]
