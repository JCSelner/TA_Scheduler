from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Semester, Course, Section, Assignment

admin.site.register(User)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Assignment)

