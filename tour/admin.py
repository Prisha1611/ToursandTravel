from django.contrib import admin

# Register your models here.

from . models import About, Home, Services, Booking, Message, Testimonial, GalleryImage


admin.site.register(About)
admin.site.register(Home)
admin.site.register(Services)
admin.site.register(Testimonial)
admin.site.register(Booking)
admin.site.register(Message)
admin.site.register(GalleryImage)
