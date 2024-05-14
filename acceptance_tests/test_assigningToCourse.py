from django.test import TestCase, Client
from project_app.models import Course, Semester, Seasons, Assignment, User,Roles


class AssignmentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(userID='user', firstName='John', lastName='Doe', email="meme@meme.com", password="test", role=Roles.TA)
        self.mane = User.objects.create(userID='mane', firstName='Jane', lastName='Doe', email="mem@meme.com", password="test", role=Roles.TA)

        self.sem = Semester.objects.create(year=2020, season= Seasons.Fall)
        self.course= Course.objects.create(courseName='Test Course', courseDescription='Test Course', courseID=1, courseSemester=self.sem)
        Assignment.objects.create(courseID=self.course, userID=self.mane)

    def test_AC1(self):
        resp = self.client.post('/assignToCourse/1/', {'User': 'user'})
        self.assertEqual(resp.context['message'], 'user is successfully assigned to Test Course')

    def test_AC2(self):
        resp = self.client.post('/assignToCourse/1/', {'User': 'mane'})
        self.assertEqual(resp.context['message'], 'mane is already assigned to the course')
