from django.contrib import admin
from .models import Doctor, Appointment, ContactUs, Email, PushMessage, Testimonial

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(ContactUs)
admin.site.register(Email)
admin.site.register(PushMessage)
admin.site.register(Testimonial)