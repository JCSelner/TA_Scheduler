from django.test import TestCase, Client
from project_app.models import Course, Semester, Seasons


class CourseCreationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.semester = Semester.objects.create(season=Seasons.Fall, year=2020)
        Course.objects.create(courseName="math101", courseSemester=self.semester, courseID=1)

    def test_AC1(self):
        resp = self.client.post('/createCourse/', {'Name': "meth101", 'Semester': "Fall 2020", 'Description': "idk"}, follow=True)
        self.assertEqual(resp.redirect_chain[0][0], "/manageCourse/", "redirected to wrong url")

    def test_AC2(self):
        resp = self.client.post('/createCourse/', {'Name': "math101", 'Semester': "Fall 2020", 'Description': "idk"}, follow=True)
        message = resp.context['errorMessage']
        self.assertEqual(message, "math101 Fall 2020 is already in the database", "failed to give error message")


