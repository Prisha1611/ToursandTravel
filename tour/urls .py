from django.urls import path
from tour import views

app_name = "tour"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('services/', views.services, name='services'),
    path('book', views.book, name='book'),
    path('bookingsuccessful/', views.bookingsuccessful, name='bookingsuccessful'),
    path('sendmessage', views.sendmessage, name='sendmessage')
]
