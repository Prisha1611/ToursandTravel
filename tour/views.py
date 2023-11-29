from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')
    
def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def services(request):
    return render(request,'services.html')