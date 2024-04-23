from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from project_app.models import User, Course, Assignment, Section, Roles
from classes.courseClass import CourseClass
from random import randint

# Create your views here.


class Courses(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses.html',{"courses": courses})

    def post(self, request):
        courses = Course.objects.all()
        print(courses)
        return render(request, "courses.html", {"courses": courses})

class CreateCourse(View):
    def get(self, request):
        return render(request, 'createCourse.html')

    def post(self, request):
        courses = Course.objects.all()
        name = request.POST.get('Name')
        semester = request.POST.get('Semester')
        description = request.POST.get('Description')
        CourseClass.createCourse(CourseClass, name, semester, len(courses)+1, description)
        courses = Course.objects.all()
        print(courses)
        return redirect('courses')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('userID')
        password = request.POST.get('password')

        if User.objects.filter(userID=username, password=password).exists():
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