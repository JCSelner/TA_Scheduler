from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from project_app.models import User, Course, Assignment, Lab, Roles


# Create your views here.


class Courses(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


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