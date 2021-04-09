from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Complain
# Register your models here.

#Admin Header
admin.site.site_header = "Obafemi Awolowo University- Enquiry Admin Panel"

#Register  Models
admin.site.register(Complain)

#Unregister Models
admin.site.unregister(Group)
