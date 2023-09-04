from django.urls import path
from . import views

urlpatterns = [
    path('user-list/', views.user_list, name='user_list'),
    path('send-message/<int:user_id>/', views.send_message, name='send_message'),
]