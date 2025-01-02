from django.contrib import admin

from .models import Citizen, Department, Employee, Service, ServiceRequest, Complaint, Post

admin.site.register(Citizen)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Complaint)
admin.site.register(ServiceRequest)
admin.site.register(Post)