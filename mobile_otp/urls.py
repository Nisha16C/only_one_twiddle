from django.urls import path
from . import views

urlpatterns = [
    #
    path('login_with_otp/', views.login_with_otp, name='login_with_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('invalid_otp/', views.verify_otp, name='invalid_otp'),
    path('register_phone_number/', views.register_phone_number, name='register_phone_number'),

]
