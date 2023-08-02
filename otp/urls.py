from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    # ...

    # Add the OTP login URL pattern
    path('login_with_otp/', views.login_with_otp, name='login_with_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
]
