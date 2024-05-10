from django.test import TestCase, Client
from project_app.models import Course, Semester, Seasons


class CourseCreationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.semester = Semester.objects.create(season=Seasons.Fall, year=2020)
        Course.objects.create(courseName="math101", courseSemester=self.semester, courseID=1)

    def test_AC1(self):
        resp = self.client.post('/createCourse/', {'Name': "meth101", 'Semester': "Fall 2035", 'Description': "idk"}, follow=True)
        self.assertEqual(resp.url, "/courses/", "redirected to wrong url")

    def test_AC2(self):
        resp = self.client.post('/createCourse/', {'Name': "math101", 'Semester': "Fall 2020", 'Description': "idk"}, follow=True)
        message = resp.context['errorMessage']
        self.assertEqual(message, "The course is invalid", "failed to give error message")


