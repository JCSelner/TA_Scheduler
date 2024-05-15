from django.test import TestCase, Client
from project_app.models import Course, Semester, Seasons, User, Assignment, SectionTypes


class CourseSectionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.semester = Semester.objects.create(season=Seasons.Fall, year=2025)
        self.sectionType = SectionTypes.Lab
        self.course = Course.objects.create(courseName="math101", courseSemester=self.semester, courseID=1)
        self.user = User.objects.create(userID='tmpUser', password='tmpPass', email="tmp@email.com", phone=1234567890,
                                        firstName="tmpFirst", lastName="tmpLast", role='TA', address="tmp House")


    def test_AC1(self):
        resp = self.client.post('/createSection/1/', {'Type': self.sectionType, 'TA': self.user}, follow=True)
        self.assertEqual(resp.redirect_chain, [], "No redirect expected")

    def test_AC2(self):
        resp = self.client.post('/createSection/1/', {'Type': self.sectionType, 'TA': self.user}, follow=True)
        message = resp.context['errorMessage']
        self.assertEqual(message, 'Section already exists', "Failed to give error message")