from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from project_app.models import User, Course, Assignment, Section, Roles, Semester, Seasons
from classes.courseClass import CourseClass



# Create your views here.


class Courses(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses.html', {"courses": courses, "seasons": Seasons.choices})

    def post(self, request):
        semesters = Semester.objects.all()
        currentYear = 2024
        courses = Course.objects.all()
        year = int(request.POST['Year'])
        season = request.POST['Season']
        if (year < currentYear):
            return render(request, 'courses.html', {"courses": courses, "seasons": Seasons.choices, "errorMessage": "The year is before the current year"})
        else:
            Semester.objects.create(year=year, season=season, semesterID=len(semesters)+1)
            return render(request, "courses.html", {"courses": courses, "seasons": Seasons.choices})


class CreateCourse(View):
    def get(self, request):
        semesters = Semester.objects.all()
        return render(request, 'createCourse.html', {"semester": semesters})

    def post(self, request):
        currentYear = 2024
        courses = Course.objects.all()
        name = request.POST.get('Name')
        semester = request.POST.get('Semester')
        description = request.POST.get('Description')
        CourseClass.createCourse(CourseClass, currentYear, name, semester, len(courses) + 1, description)
        courses = Course.objects.all()
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


class ManageUser(View):
    def get(self, request):
        return render(request, 'account.html')

    def post(self, request):
        pass


class CreateUser(View):
    def get(self, request):
        return render(request, 'createUser.html', {'roles': Roles.choices})

    def post(self, request):
        username = request.POST['userID']
        password = request.POST['password']
        email = request.POST['email']
        contact_number = request.POST['phone']
        address = request.POST['address']
        role = request.POST['role']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']

        User.objects.create(userID=username,
                            password=password,
                            email=email,
                            phone=contact_number,
                            address=address,
                            role=role,
                            firstName=first_name,
                            lastName=last_name)
        return render(request, 'createUser.html', {'roles': Roles.choices})


class DeleteUser(View):
    def get(self, request):
        users = User.objects.filter().all()
        return render(request, 'deleteUser.html',
                      {'roles': Roles.choices,
                       'users': users})

    def post(self, request):
        # query (filter) for users
        users = User.objects.filter().all()
        return render(request, 'deleteUser.html',
                      {'roles': Roles.choices,
                       'users': users})


class ExtendDeleteUsers(View):
    def post(self, request):
        users = User.objects.filter().all()
        user_id = request.POST.get('userID')
        user = User.objects.get(userID=user_id)
        user.delete()
        return render(request, 'deleteUser.html',
                      {'roles': Roles.choices,
                       'users': users})