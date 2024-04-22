from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Course, Assignment, Section

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Section)
