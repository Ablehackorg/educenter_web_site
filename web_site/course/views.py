from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from home.models import Setting


def about(request):
    return render(request,'about.html')
    # return render(request, 'index.html')

def courses(request):
    return render(request,'')