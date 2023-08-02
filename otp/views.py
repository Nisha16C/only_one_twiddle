from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from twilio.rest import Client
from django.conf import settings
import random
import requests

def login_with_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        # Generate and send OTP
        otp = generate_otp()
        send_otp(phone_number, otp)
        request.session['phone_number'] = phone_number
        request.session['otp'] = otp
        return redirect('verify_otp')
    return render(request, 'account/login_with_otp.html')

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(phone_number, otp):
    # Your Twilio account SID and authentication token
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    # Your Twilio phone number (must be verified on Twilio)
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"OTP sent via SMS to {phone_number}: {otp}")
        return True
    except Exception as e:
        # Handle exceptions here (e.g., TwilioRestException)
        print(f"Failed to send OTP via SMS to {phone_number}: {e}")
        return False

def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if otp_entered == stored_otp:
            phone_number = request.session.get('phone_number')
            user, _ = User.objects.get_or_create(username=phone_number)
            user = authenticate(request, username=phone_number)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your home page URL
        else:
            context = {'error_message': 'Invalid OTP'}
            return render(request, 'account/verify_otp.html', context)
    return render(request, 'account/verify_otp.html')

