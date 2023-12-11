from django.db import models

# Create your models here.

class About(models.Model):
    description = models.TextField(max_length=7000, blank=False)
    img1 = models.ImageField(upload_to='aboutpage', default='about.jpg')
    img2 = models.ImageField(upload_to='aboutpage', default='about.jpg')
    img3 = models.ImageField(upload_to='aboutpage', default='about.jpg')
    img4 = models.ImageField(upload_to='aboutpage', default='about.jpg')
    img5 = models.ImageField(upload_to='aboutpage', default='about.jpg')

    def __str__(self):
        return self.description

class Home(models.Model):
    description = models.TextField(max_length=7000, blank=False)
    img1 = models.ImageField(upload_to='homepage', default='home.jpg')
    img2 = models.ImageField(upload_to='homepage', default='home.jpg')
    img3 = models.ImageField(upload_to='homepage', default='home.jpg')
    def __str__(self):
        return self.description


class Services(models.Model):
    description = models.TextField(max_length=7000, blank=False)
    img1 = models.ImageField(upload_to='servicespage', default='services.jpg')
    img2 = models.ImageField(upload_to='servicespage', default='services.jpg')
    img3 = models.ImageField(upload_to='servicespage', default='services.jpg')
    img4 = models.ImageField(upload_to='servicespage', default='services.jpg')

    def __str__(self):
        return self.description


class Booking(models.Model):
    fullname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    travel_date = models.CharField(max_length=100, blank=True)
    return_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.fullname


class Message(models.Model):
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.fname

class Testimonials(models.Model):
    description = models.TextField(max_length=7000, blank=False)
    img1 = models.ImageField(upload_to='test', default='test.jpg')
    img2 = models.ImageField(upload_to='test', default='test.jpg')
    img3 = models.ImageField(upload_to='test', default='test.jpg')

    def __str__(self):
        return self.description