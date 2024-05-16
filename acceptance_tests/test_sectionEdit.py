from django.test import TestCase, Client
from django.urls import reverse
from project_app.models import Course, Semester, Seasons, User, Assignment, Section


class CourseSectionTestCase(TestCase):
    def setUp(self):
        client = Client()
        self.semester = Semester.objects.create(season=Seasons.Fall, year=2025)
        self.course = Course.objects.create(courseName="math101", courseSemester=self.semester, courseID=1)
        self.user = User.objects.create(userID='tmpUser', password='tmpPass', email="tmp@email.com", phone=1234567890,
                                        firstName="tmpFirst", lastName="tmpLast", role='TA', address="tmp House")
        self.user2 = User.objects.create(userID='tmpUser2', password='tmpPass2', email="tmp2@email.com", phone=1234567891,
                                        firstName="tmpFirst2", lastName="tmpLast2", role='TA', address="tmp House2")
        self.section = Section.objects.create(sectionID=1, type="Lab", course=self.course, taID=self.user)

    def test_AC1(self):
        client = Client()
        response = client.post('/editSection/1/', {'section': self.section, 'type': "Lecture", 'user': self.user2}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.section.refresh_from_db()
        self.assertEqual(self.section.type, "Lecture")
        self.assertEqual(self.section.taID, self.user2)
