"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from project_app.views import (Courses, Login, Logout, Home, InstructorHome, TeachingAssistantHome, CreateCourse,
                               ManageUser, ManageAccount, CreateUser, DeleteUser, ExtendDeleteUsers, ExtendDeleteCourse,
                               ManageCourse, EditUser, CourseDisplay, UserDisplay, CreateSection, EditSection,
                               AssignToCourse, InstructorCoursePage, DeleteSection)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),
    path('home/instructor/', InstructorHome.as_view(), name='instructor_home'),
    path('home/teachingAssistant/', TeachingAssistantHome.as_view(), name='teaching_assistant_home'),
    path('manageUser/', ManageUser.as_view(), name='manageUser'),
    path('manageAccount/instructor/<int:pk>/', ManageAccount.as_view(), name='instructor_account'),
    path('createUser/', CreateUser.as_view(), name='createUser'),
    path('deleteUser/', DeleteUser.as_view(), name='deleteUser'),
    path('deletedUser/', ExtendDeleteUsers.as_view(), name='extendDeleteUser'),
    path('courses/', Courses.as_view(), name='courses'),
    path('courses/instructor/', InstructorCoursePage.as_view(), name='instructorCoursePage'),
    path('deleteCourse/', ExtendDeleteCourse.as_view(), name='extendDeleteCourse'),
    path('logout/', Logout.as_view(), name='logout'),
    path('createCourse/', CreateCourse.as_view(), name='createCourse'),
    path('editUser/<int:pk>/', EditUser.as_view(), name='editUser'),
    path('manageCourse/', ManageCourse.as_view(), name='manageCourse'),
    path('courseDisplay/<int:pk>/', CourseDisplay.as_view(), name='courseDisplay'),
    path('userDisplay/<int:pk>/', UserDisplay.as_view(), name='userDisplay'),
    path('assignToCourse/<int:pk>/', AssignToCourse.as_view(), name='assignToCourse'),
    path('createSection/<int:pk>/', CreateSection.as_view(), name='createSection'),
    path('editSection/<int:pk>/', EditSection.as_view(), name='editSection'),
    path('deleteSection/<int:pk>/', DeleteSection.as_view(), name='deleteSection')
]
