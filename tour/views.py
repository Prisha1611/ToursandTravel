from django.contrib import messages
from django.shortcuts import render, redirect
from .models import About, Home, Services, Booking, Message, Testimonials


# Create your views here.
def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {"about": about})


def contact(request):

    return render(request, 'contact.html')


def sendmessage(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        query = Message(fname=fname, lname=lname, email=email, message=message)
        query.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('/contact')

    return render(request, 'contact.html')


def elements(request):
    testimonials = Testimonials.objects.all()
    return render(request, 'elements.html')


def index(request):
    # home = Home.objects.all()
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def services(request):
    services = Services.objects.all()
    return render(request, 'services.html')


def book(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        travel_date = request.POST.get('travel_date')
        return_date = request.POST.get('return_date')

        query = Booking(fullname=fullname, phone=phone, email=email, destination=destination,
                        travel_date=travel_date, return_date=return_date)
        query.save()
        return redirect('/bookingsuccessful')

    return render(request, 'index.html')


def bookingsuccessful(request):
    return render(request, 'bookingsuccessful.html')


