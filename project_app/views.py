from django.shortcuts import render, redirect
from django.views import View
from project_app.models import User, Course, Assignment, Section, Roles, Semester, Seasons, SectionTypes
from classes.accounts import Account
from classes.courseClass import CourseClass
from classes.section import SectionClass
from django.http import HttpResponse
from classes.assignmentClass import AssignmentClass


# Create your views here.


class Courses(View):
    def get(self, request):
        try:
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        courses = Course.objects.all()
        return render(request, 'courses.html',
                      {
                          "courses": courses,
                          'user_session': s,
                          'role': role,
                      })

    def post(self, request):
        semesters = Semester.objects.all()
        currentYear = 2024
        courses = Course.objects.all()
        try:
            year = int(request.POST['Year'])
        except(ValueError):
            return render(request, 'createCourse.html',
                          {
                              "courses": courses,
                              "seasons": Seasons.choices,
                              "semester": semesters,
                              "semErrorMessage": "The year must not be blank"
                          })

        season = request.POST['Season']
        if (year < currentYear):
            return render(request, 'createCourse.html',
                          {
                              "courses": courses,
                              "seasons": Seasons.choices,
                              "semester": semesters,
                              "semErrorMessage": "The year must be at least " + str(currentYear)
                          })
        if (len(Semester.objects.filter(year=year, season=season)) != 0):
            return render(request, 'createCourse.html',
                          {
                              "courses": courses,
                              "seasons": Seasons.choices,
                              "semester": semesters,
                              "semErrorMessage": season + " " + year.__str__() + " is already in the database"
                          })
        else:
            Semester.objects.create(year=year, season=season, semesterID=len(semesters) + 1)
            return render(request, "createCourse.html",
                          {
                              "courses": courses,
                              "seasons": Seasons.choices,
                              "semester": semesters,
                              "errorMessage": ""
                          })


class ExtendDeleteCourse(View):
    def post(self, request):
        courses = Course.objects.all()
        course_id = request.POST.get('courseID')
        courseID = int(course_id)
        Course.objects.filter(courseID=courseID).delete()
        return render(request, "courses.html",
                      {
                          "courses": courses,
                          "seasons": Seasons.choices,
                          "errorMessage": ""
                      })


class ManageCourse(View):

    def get(self, request):
        try:
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        return render(request, 'manageCourses.html',
                      {
                          'role': role,
                          'user_session': s
                      })


class CreateCourse(View):
    def get(self, request):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        semesters = Semester.objects.all()
        return render(request, 'createCourse.html',
                      {
                          "semester": semesters,
                          'user_session': s,
                          "seasons": Seasons.choices,
                          "errorMessage": ""
                      })

    def post(self, request):
        currentYear = 2024
        courses = Course.objects.all()
        name = request.POST.get('Name')
        semesterName = request.POST.get('Semester')
        semesterFields = semesterName.split(' ')
        semester = Semester.objects.filter(year=int(semesterFields[1]), season=semesterFields[0])
        if len(courses) == 0:
            courseID = 1
        else:
            courseID = courses[len(courses) - 1].courseID + 1

        description = request.POST.get('Description')
        if (CourseClass.createCourse(CourseClass, name, semester[0], courseID, description)):
            return redirect("/manageCourse/")
        else:
            semesters = Semester.objects.all()
            return render(request, 'createCourse.html',
                          {
                              "semester": semesters,
                              "seasons": Seasons.choices,
                              "errorMessage": name + " " + semester[0].__str__() + " is already in the database"
                          })


class Login(View):
    # Handle the HTTP GET request by rendering the 'login.html' file.
    def get(self, request):
        return render(request, 'login.html')

    # Handle the HTTP POST request by managing the data submitted by the 'login.html' file.
    def post(self, request):
        # Extract the data from the submitted form.
        username = request.POST["userID"]
        password = request.POST["password"]

        if User.objects.filter(userID=username, password=password).exists():
            # Store the name of the user in the session data associated with the current request.
            request.session['userID'] = request.POST["userID"]
            # Determine the role of the user based on their 'username' and 'password'.
            user_role = User.objects.filter(userID=username, password=password).values('role')
            # Verify their role and redirect to appropriate homepage.
            # Also, the user's role becomes stored in the session data.
            # This is done to carry over the role of the user to different pages,
            # allowing for different functionality to be managed such as redirecting based on role,
            # or denying certain actions from being displayed.
            for role in user_role:
                if role['role'] == 'Admin':
                    request.session['role'] = role['role']
                    return redirect('home')
                elif role['role'] == 'Instructor':
                    request.session['role'] = role['role']
                    return redirect('instructor_home')
                elif role['role'] == 'TA':
                    request.session['role'] = role['role']
                    return redirect('teaching_assistant_home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html',
                          {
                              'error_message': error_message
                          })


class Home(View):
    # Upon a successful redirect, from 'login.html' to 'home.html'
    # Handle the HTTP GET request, by simply rendering the 'home.html' page.
    def get(self, request):
        try:
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        return render(request, 'home.html',
                      {
                          'role': role,
                          'user_session': s
                      })


class InstructorHome(View):
    def get(self, request):
        try:
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        users = User.objects.filter(userID=s).all()
        return render(request, 'instructor_home.html',
                      {
                          'user_session': s,
                          'role': role,
                          'users': users
                      })


class InstructorCoursePage(View):
    def get(self, request):
        try:
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        courses = Course.objects.all()
        return render(request, 'view_courses.html',
                      {
                          'user_session': s,
                          'courses': courses,
                          'role': role,
                          'season': Seasons.choices
                      })


class TeachingAssistantHome(View):
    def get(self, request):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        return render(request, 'teaching_assistant_home.html', {'user_session': s})


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
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        return render(request, 'account.html',
                      {
                          'role': role,
                          'user_session': s
                      })


class ManageAccount(View):
    def get(self, request, pk):
        try:
            # Carry along the session of the current user to the 'account.html' page.
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        user = User.objects.get(pk=pk)
        return render(request, 'manage_account.html',
                      {
                          'user': user,
                          'user_session': s
                      })

    def post(self, request, pk):
        account = Account()
        user = User.objects.get(pk=pk)

        # Gather all the data from the user
        user_data = {
            'userID': request.POST.get('username'),
            'firstName': request.POST.get('firstName'),
            'lastName': request.POST.get('lastName'),
            'phone': request.POST.get('phoneNumber'),
            'email': request.POST.get('email'),
            'address': request.POST.get('address')
        }

        # Use the edit_user method to update the user instance
        account.edit_user(user, **user_data)

        # Save the changes to the user instance
        user.save()
        confirmation_message = 'User Updated Successfully!'
        return render(request, 'manage_account.html',
                      {
                          'user': user,
                          'confirmation_message': confirmation_message
                      })
        # return HttpResponse('User Updated Successfully')


class CreateUser(View):
    def get(self, request):
        try:
            # Carry along the session of the current user to the 'createUser.html' page.
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        return render(request, 'createUser.html',
                      {
                          'roles': Roles.choices,
                          'user_session': s,
                          'errorMessage': ''
                      })

    def post(self, request):
        username = request.POST['userID']
        password = request.POST['password']
        email = request.POST['email']
        contact_number = request.POST['phone']
        address = request.POST['address']
        role = request.POST['role']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        if (User.objects.filter(userID=username).exists() or User.objects.filter(email=email).exists()):
            return render(request, 'createUser.html',
                          {
                              'roles': Roles.choices,
                              'errorMessage': 'Username or email is already in use.'
                          })
        else:
            User.objects.create(userID=username,
                                password=password,
                                email=email,
                                phone=contact_number,
                                address=address,
                                role=role,
                                firstName=first_name,
                                lastName=last_name)
            return render(request, 'createUser.html',
                          {
                              'roles': Roles.choices,
                              'errorMessage': ''
                          })


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
                      {
                          'roles': Roles.choices,
                          'users': users
                      })


class ExtendDeleteUsers(View):
    def post(self, request):
        users = User.objects.filter().all()
        user_id = request.POST.get('userID')
        user = User.objects.get(userID=user_id)
        user.delete()
        return render(request, 'deleteUser.html',
                      {
                          'roles': Roles.choices,
                          'users': users
                      })


class UserDisplay(View):

    def get(self, request, pk):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        user = User.objects.get(pk=pk)
        assignments = Assignment.objects.filter(userID=user)
        sections = Section.objects.filter(taID=user)
        return render(request, 'userDisplay.html',
                      {
                          'user_session': s,
                          'user': user,
                          'assignments': assignments,
                          'sections': sections
                      })


class CourseDisplay(View):
    def get(self, request, pk):
        try:
            role = request.session['role']
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        course = Course.objects.get(courseID=pk)
        assignments = Assignment.objects.filter(courseID=course)
        sections = Section.objects.filter(course=course)
        return render(request, 'courseDisplay.html',
                      {
                          'course': course,
                          'assignments': assignments,
                          'sections': sections,
                          'user_session': s,
                          'role': role
                      })


class EditUser(View):
    def get(self, request, pk):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        user = User.objects.get(pk=pk)
        return render(request, 'editUser.html',
                      {
                          'user_session': s,
                          'user': user
                      })

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.role = request.POST.get('role')
        user.address = request.POST.get('address')
        user.save()
        return HttpResponse('User updated successfully')


class CreateSection(View):
    def get(self, request, pk):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        course = Course.objects.get(courseID=pk)
        taAssigments = Assignment.objects.filter(courseID=course)
        tas = []
        for ta in taAssigments:
            tas.append(ta.userID)

        return render(request, 'createSection.html',
                      {
                          'user_session': s,
                          'course': course,
                          'taID': tas,
                          'types': SectionTypes.choices,
                          'errorMessage': ""
                      })

    def post(self, request, pk):
        course = Course.objects.get(courseID=pk)
        sections = Section.objects.all()
        if len(sections) == 0:
            sectionID = 1
        else:
            sectionID = sections[len(sections) - 1].sectionID + 1
        type = request.POST.get('type')
        taName = request.POST.get('TA')
        taID = User.objects.get(userID=taName)
        taAssigments = Assignment.objects.filter(courseID=course)
        tas = []
        for ta in taAssigments:
            tas.append(ta.userID)
        if (SectionClass.createSection(SectionClass, sectionID=sectionID, type=type, course=course, taID=taID)):
            return render(request, 'createSection.html',
                          {
                              'course': course,
                              'taID': tas,
                              'types': SectionTypes.choices,
                              'errorMessage': "Section created successfully"
                          })
        else:

            return render(request, 'createSection.html',
                          {
                              'course': course,
                              'taID': tas,
                              'types': SectionTypes.choices,
                              'errorMessage': "Failed to create Section."
                          })


class EditSection(View):
    def get(self, request, pk):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        section = Section.objects.get(sectionID=pk)
        course = section.course
        taAssigments = Assignment.objects.filter(courseID=course)
        tas = []
        for ta in taAssigments:
            tas.append(ta.userID)
        return render(request, 'editSection.html',
                      {
                          'user_session': s,
                          'course': course,
                          'section': section,
                          'taID': tas,
                          'types': SectionTypes.choices
                      })

    def post(self, request, pk):
        section = Section.objects.get(pk=pk)
        section.type = request.POST.get('type')
        taName = request.POST.get('taID')
        section.taID = User.objects.get(userID=taName)
        section.save()
        return HttpResponse("Section updated successfully")


class AssignToCourse(View):
    def get(self, request, pk):
        try:
            s = request.session['userID']
        except KeyError:
            return redirect('login')
        course = Course.objects.get(courseID=pk)
        assignments = Assignment.objects.filter(courseID=course)
        users = User.objects.all().exclude(role=Roles.ADMIN)
        return render(request, 'user2course.html',
                      {
                          'user_session': s,
                          'assignments': assignments,
                          'users': users,
                          'course': course,
                          'message': ''
                      })

    def post(self, request, pk):
        course = Course.objects.get(courseID=pk)
        user = User.objects.get(userID=request.POST.get('User'))
        assignments = Assignment.objects.filter(courseID=course)
        users = User.objects.all().exclude(role=Roles.ADMIN)
        if (AssignmentClass.assignUser(AssignmentClass, user.userID, course.courseID)):
            return render(request, 'user2course.html',
                          {
                              'assignments': assignments,
                              'users': users,
                              'course': course,
                              'message': user.userID + ' is successfully assigned to ' + course.courseName
                          })
        else:
            return render(request, 'user2course.html',
                          {
                              'assignments': assignments,
                              'users': users,
                              'course': course,
                              'message': user.userID + ' is already assigned to the course'
                          })
