from django.test import TestCase, Client
from project_app.models import Course, Semester, Seasons


class CourseDeletionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.semester = Semester.objects.create(season=Seasons.Fall, year=2020)
        Course.objects.create(courseName="math101", courseSemester=self.semester, courseID=1)

    def test_AC1(self):
        resp = self.client.post('/deleteCourse/', {'courseID': 1})
        courses = Course.objects.all()
        self.assertEqual(len(courses), 0, "failed to delete course")
