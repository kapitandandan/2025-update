from django.contrib import admin

from .models import Citizen, Service,  Complaint, Post, Feedback

admin.site.register(Citizen)
admin.site.register(Service)
admin.site.register(Complaint)
admin.site.register(Post)
admin.site.register(Feedback)