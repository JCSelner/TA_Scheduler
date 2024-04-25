from django.db import models


# Create your models here.

class Roles(models.TextChoices):
    INSTRUCTOR = "Instructor"
    TA = "TA"
    ADMIN = "Admin"


class SectionTypes(models.TextChoices):
    Lecture = "Lecture"
    Lab = "Lab"

class Seasons(models.TextChoices):
    Summer = "Summer"
    Winter = "Winter"
    Fall = "Fall"
    Spring = "Spring"


class User(models.Model):
    userID = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=13, choices=Roles.choices, default=Roles.ADMIN)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return (self.userID
                + " " + self.firstName
                + " " + self.lastName
                + " " + self.email
                + " " + self.phone
                + " " + self.address)


class Semester(models.Model):
    season = models.CharField(max_length=13, choices=Seasons.choices)
    year = models.IntegerField()
    semesterID = models.IntegerField()

    def __str__(self):
        return self.season + " " + self.year.__str__()


class Course(models.Model):
    courseName = models.CharField(max_length=50)
    courseDescription = models.CharField(max_length=1000)
    courseID = models.IntegerField(primary_key=True)
    courseSemester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseName + " " + self.courseSemester.__str__()


class Assignment(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseID.__str__() + " " + self.userID.__str__()


class Section(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    taID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sectionID = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=SectionTypes.choices)

    def __str__(self):
        return self.sectionID + " " + self.type
