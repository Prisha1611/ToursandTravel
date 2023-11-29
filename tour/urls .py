from django.urls import path
from tour import views
app_name="tour"

urlpatterns =[
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('', views.index),
    path('main', views.main, name='main'),
    path('services', views.services, name='services'),
]