from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
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
            return render(request, 'courses.html', {"courses": courses, "seasons": Seasons.choices,
                                                    "errorMessage": "The year is before the current year"})
        else:
            Semester.objects.create(year=year, season=season, semesterID=len(semesters) + 1)
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
    # Handle the HTTP GET request by rendering the 'login.html' file.
    def get(self, request):
        return render(request, 'login.html')

    # Handle the HTTP POST request by managing the data submitted by the 'login.html' file.
    def post(self, request):
        # Extract the data from the submitted form.
        username = request.POST["userID"]
        password = request.POST["password"]

        # Query the database and check if the user exists in the database.
        # We check by calling the 'exists()' function on the filtered Object call.
        if User.objects.filter(userID=username, password=password).exists():
            # If the user exists in the database,
            # Store the name of the user in the session data associated with the current request.
            request.session['userID'] = request.POST["userID"]
            # Redirect the user towards the homepage.
            return redirect('home')
        else:
            # Otherwise, render the 'login.html' page, displaying an error message.
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})


class Home(View):
    # Upon a successful redirect, from 'login.html' to 'home.html'
    # Handle the HTTP GET request, by simply rendering the 'home.html' page.
    def get(self, request):
        try:
            # Carry along the session of the current user to the 'home.html' page.
            # The try-except block will handle the 'KeyError' exception,
            # Which raises if there's no existing session with the given 'userID' key.
            s = request.session['userID']
        except KeyError:
            # If the KeyError exception is caught, simply redirect to the 'login.html' page.
            return redirect('login')
        return render(request, 'home.html', {'user_session': s})


class Logout(View):
    def get(self, request):
        # Upon a successful logout request, remove the specific user from the session via the provided key.
        # If the provided key, does not exist, simply return 'None'.
        request.session.pop('userID', None)
        # Finally, redirect the user back to the 'login.html' page.
        return redirect('login')


class ManageUser(View):
    def get(self, request):
        try:
            # Carry along the session of the current user to the 'account.html' page.
            s = request.session['userID']
        except KeyError:
            # Handle 'KeyError' exceptions appropriately
            return redirect('login')
        return render(request, 'account.html', {'user_session': s})


class CreateUser(View):
    def get(self, request):
        try:
            # Carry along the session of the current user to the 'createUser.html' page.
            s = request.session['userID']
        except KeyError:
            # Handle 'KeyError' exceptions appropriately
            return redirect('login')
        return render(request, 'createUser.html', {'roles': Roles.choices, 'user_session': s})

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
        try:
            # Carry along the session of the current user to the 'deleteUser.html' page.
            s = request.session['userID']
        except KeyError:
            # Handle 'KeyError' exceptions appropriately
            return redirect('login')
        users = User.objects.filter().all()
        return render(request, 'deleteUser.html',
                      {
                          'roles': Roles.choices,
                          'users': users,
                          'user_session': s
                      })

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
