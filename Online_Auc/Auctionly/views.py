from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,  login
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')

def sign_in(request):

    if request.method == 'POST':

        # retrives username and pass from the form submitted by user
        
        username = request.POST.get('username')
        password = request.POST.get('password')


        # check if the username exist in database or not
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found')
            return redirect('/sign_in')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()

        if not profile_obj.is_verified:
            messages.success(request, "Profile isn't verified check your mail")
            return redirect('/sign_in')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.success(request, "Wrong Password")
            return redirect('/sign_in')
        
        login(request, user)
        return redirect('/')


    return render(request, 'signin.html')

def sign_up(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is already taken.')
                return redirect('/sign_up')
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email already in use.')
                return redirect('/sign_up')

            user_obj = User.objects.create(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('/emailsent')
        
        except Exception as e:
            print(e)


    return render(request, 'signup.html')

def success(request):
    return render(request, 'Auctionly.html')

def aboutAuctionly(request):
    return render(request, 'aboutAuctionly.html')

def contactUs(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        mobile = request.POST.get('mobile')
        text = request.POST.get('text')
        contact.name = name
        contact.mail = mail
        contact.mobile = mobile
        contact.text = text
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACTING AUCTIONLY</h1>")
    return render(request, 'contactUs.html')

def departmentAuctionly(request):
    return render(request, 'departmentAuctionly.html')

def liveauction(request):
    return render(request, 'liveauction.html')

def pastauction(request):
    return render(request, 'pastauction.html')

def upcomingauction(request):
    return render(request, 'upcomingauction.html')

def emailsent(request):
    return render(request, 'emailsent.html')

# veryfying the authetication link shared

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account has already been verified.')
                return redirect('/sign_in')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Congrats your account has been verified.')
            return redirect('/sign_in')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)





# fxn for sending email for authetication

def send_mail_after_registration(email, token):
    subject = 'Your acc needs to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)