from allauth.account.auth_backends import AuthenticationBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, get_backends
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth.decorators import login_required


from .models import PhoneNumber
import random  # For generating OTP (replace with your OTP generation logic)
import twilio



def login_with_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = generate_otp()
        send_otp(phone_number, otp)
        try:
            phone_obj = PhoneNumber.objects.get(phone_number=phone_number)
            user = phone_obj.user
        except PhoneNumber.DoesNotExist:
            messages.error(request, 'Mobile number is not registered.')
            return redirect('login_with_otp')
      
        
        # Store phone number, user, and OTP in session
        request.session['phone_number'] = phone_number
        request.session['user_id'] = user.id
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
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')
        
        if entered_otp == saved_otp:
            user_id = request.session.get('user_id')
            # password = "linux"
            user = User.objects.get(id=user_id)
            print("before authentication")
            authenticated = True
            print("after authentication")
            
            try:               
               
                if authenticated: 
                    print("user authentcated")  
                    user.backend = 'allauth.account.auth_backends.AuthenticationBackend'               
                    login(request, user)
                    return redirect('home')  # Redirect to home page
                else:
                    print("user not authentcated") 
                    # print("no authenticate")
                    messages.error(request, 'Authentication failed. Please contact support.')
                    return redirect('login_with_otp')
                
            except Exception as e:   
                print("Exception during authentication:", e)
                messages.error(request, 'Authentication failed. Please contact support.')
                return redirect('login_with_otp')
            
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('invalid_otp')
    
    return render(request, 'account/verify_otp.html')


@login_required
def register_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST.get('mobile_number')
        print(phone_number)
        if phone_number:
            PhoneNumber.objects.create(user=request.user, phone_number=phone_number)
            messages.success(request, 'Mobile number registered successfully.')
            return redirect('profile', request.user)
        else:
            messages.error(request, 'Please provide a valid phone number.')
    
    return render(request, 'profiles/add_mobile.html')


