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

from project_app.views import (Courses, Login, Logout, Home, CreateCourse, ManageUser, CreateUser, DeleteUser,
                               ExtendDeleteUsers, ExtendDeleteCourse,ManageCourse)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),
    path('manageUser/', ManageUser.as_view(), name='manageUser'),
    path('createUser/', CreateUser.as_view(), name='createUser'),
    path('deleteUser/', DeleteUser.as_view(), name='deleteUser'),
    path('deletedUser/', ExtendDeleteUsers.as_view(), name='extendDeleteUser'),
    path('manageCourse/', ManageCourse.as_view(), name='manageCourse'),
    path('deleteCourses/', Courses.as_view(), name='deleteCourse'),
    path('deleteCourse/', ExtendDeleteCourse.as_view(), name='extendDeleteCourse'),
    path('home/logout/', Logout.as_view(), name='logout'),
    path('createCourse/', CreateCourse.as_view(), name='createCourse'),
]
