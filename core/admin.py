from django.contrib import admin
from .models import Student
# Register your models here.

#Admin Header
admin.site.site_header = "Obafemi Awolowo University- Enquiry Admin Panel"


admin.site.register(Student)
