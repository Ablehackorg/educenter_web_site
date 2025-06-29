from Demos.win32ts_logoff_disconnected import username
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
from home.models import Setting
from course.models import Subject,Course

from course.models import Tutor
from home.models import ContactForm, ContactMessage
from django.utils import translation

from home.models import SettingLang

from course.models import SubjectLang
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return HttpResponseRedirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return HttpResponseRedirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return HttpResponseRedirect('/home/')

    # Render the login page template (GET request)
    return render(request, 'login.html')


# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return HttpResponseRedirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return HttpResponseRedirect('/register/')

    # Render the registration page template (GET request)
    return render(request, 'register.html')


def index(request):
    # return HttpResponse("Hello Django.COM")
    setting = Setting.objects.get()
    course= Course.objects.all()
    course_cr= Course.objects.all().order_by('id')[:4]
    subject_cr= Subject.objects.all().order_by('id')[:3]

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]

    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)
        subject_cr = SubjectLang.objects.filter(lang=currentlang).order_by('subject__id')
        tutor_cr= Tutor.objects.filter(tutorlang__lang =currentlang).order_by('id')

    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    page= "home"
    context = {'setting': setting,
               'page':page,
               'subject_cr':subject_cr,
               'course_cr':course_cr,
               'course':course,
               'tutor_cr':tutor_cr}
    return render(request,'index.html',context)


def tutor(request):
    tutor_cr = Tutor.objects.all().order_by('id')
    setting = Setting.objects.get()
    context={"tutor_cr":tutor_cr,
             "setting":setting}
    return render(request,'tutors.html',context)

def about(request):
    return render(request,'about.html')
    # return render(request, 'index.html')

TELEGRAM_BOT_TOKEN = '7950108089:AAHKsk74K7yVnRqPGF5Waw_ur95YGjqZ0tI'
TELEGRAM_CHANNEL = '@azamat123Py'
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']

            message_text = f'New message:\nName: {name} \nPhone: {phone} \nSubject: {subject} \nMessage: {message}'
            telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            telegram_params = {'chat_id': TELEGRAM_CHANNEL, 'text': message_text}

            requests.post(telegram_api_url, params=telegram_params)

            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks, " + data.name + " We received your message and will respond shortly...")
            return HttpResponseRedirect('/contact/')



    setting = Setting.objects.get()
    form = ContactForm()
    context = {'setting': setting}
    return render(request, 'contact.html', context)


def subject_detail(request, id, slug):
    course = Course.objects.all()
    subject = Subject.objects.get(pk=id)

    subject_cr= Subject.objects.all().order_by('id')[:4]
    context ={
        'subject': subject,
        'course': course,
        'subject_cr': subject_cr
    }
    return render(request,'subject_detail.html',context)
def subject(request):
    subject_cr = Subject.objects.all().order_by('id')

    setting = Setting.objects.get()
    context = {'subject_cr': subject_cr,
               'setting': setting}
    return render(request, "subject.html", context)
def selectlanguage(request):
    if request.method == "POST":
        lang = request.POST['language']
        translation.activate(lang)
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang

        return HttpResponseRedirect(f"/{lang}/")




# def contact(request):
#     return render(request,'contact.html')
