from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from project_app.models import User, Course, Assignment, Lab, Roles
from classes.courseClass import CourseClass
from random import randint

# Create your views here.


class Courses(View):
    def get(self, request):
        return render(request, 'courses.html')

    def post(self, request):
        courses = Course.objects.all()
        return render(request, "courses.html", {"courses": courses})

class CreateCourse(View):
    def get(self, request):
        return render(request, 'createCourse.html')

    def post(self, request):
        courses = Course.objects.all()
        name = request.POST.get('name')
        semester = request.POST.get('semester')
        description = request.POST.get('description')
        CourseClass.createCourse(name, semester, len(courses)+1, description)
        return render(request, "courses.html", {"courses": courses})


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('userID')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})


class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')