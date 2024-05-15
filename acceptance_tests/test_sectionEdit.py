from django.test import TestCase, Client
from project_app.models import Course, Semester, Seasons, User, Assignment


class CourseSectionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.semester = Semester.objects.create(season=Seasons.Fall, year=2025)
        self.course = Course.objects.create(courseName="math101", courseSemester=self.semester, courseID=1)
        self.user = User.objects.create(userID='tmpUser', password='tmpPass', email="tmp@email.com", phone=1234567890,
                                        firstName="tmpFirst", lastName="tmpLast", role='TA', address="tmp House")

    def test_AC1(self):
        resp = self.client.post('/editSection/', {'Type': self.semester, 'TA': self.user}, follow=True)
        self.assertEqual(resp.redirect_chain, [], "No redirect expected")

    def test_AC2(self):
        resp = self.client.post('/createSection/', {'Type': self.semester, 'TA': self.semester}, follow=True)
        message = resp.context['errorMessage']
        self.assertEqual(message, 'Section successfully created', "Failed to give error message")