# new_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send-message/<int:user_id>/', views.send_message_view, name='send_message'),
    path('delete_message/<int:message_id>/', views.delete_message_view, name='delete_message'),
    # path('delete/', views.delete_chat, name= 'delete_message'),
    # Other URL patterns for your app
]
