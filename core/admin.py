from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Student
# Register your models here.

#Admin Header
admin.site.site_header = "Obafemi Awolowo University- Enquiry Admin Panel"

#Register  Models
admin.site.register(Student)

#Unregister Models
admin.site.unregister(Group)
