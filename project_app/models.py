from django.db import models


# Create your models here.

class Roles(models.TextChoices):
    instructor = "I"
    ta = "T"
    admin = "A"

class SectionTypes(models.TextChoices):
    Lecture = "Lecture"
    Lab = "Lab"

class User(models.Model):
    userID = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=1, choices=Roles.choices)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.email + " " + self.phone + " " + self.address


class Course(models.Model):
    courseName = models.CharField(max_length=50)
    courseDescription = models.CharField(max_length=1000)
    courseID = models.IntegerField(primary_key=True)
    courseSemester = models.CharField(max_length=10)

    def __str__(self):
        return self.courseName + " " + self.courseSemester


class Assignment(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseID.__str__() + " " + self.userID.__str__()


class Section(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    taID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    labID = models.CharField(max_length=20)
    type = models.Charfield(max_length=10, choices=SectionTypes.choices)

    def __str__(self):
        return self.taID.__str__() + " " + self.courseID.__str__() + " " + self.labID.__str__()
