from django.contrib import admin

# Register your models here.
from WebApp.models import StudentApplication,StaffRegistration,SRegistration

admin.site.register(StudentApplication)
admin.site.register(SRegistration)
admin.site.register(StaffRegistration)