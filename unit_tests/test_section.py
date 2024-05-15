from classes.section import SectionClass
from classes.courseClass import CourseClass
from classes.accounts import Account
from project_app.models import Section, Course, Semester, Seasons, User, Roles
from django.test import TestCase
import unittest

class testCreateSection(TestCase):

    def setUp(self):
       self.section = SectionClass()
       self.course = CourseClass()
       self.role = Roles.TA
       self.user= User.objects.create(userID='testuser', password='testpass', email='test@test.com', phone='1234567890',
                                      address='testaddress', role=self.role, firstName='testfirst', lastName='testlast')
       self.season=Seasons.Fall
       self.semester1 = Semester.objects.create(season=self.season, year=2024)
       self.semester2 = Semester.objects.create(season=self.season, year=2025)
       self.courseA = Course.objects.create(courseName='A', courseDescription='test', courseID=1, courseSemester=self.semester1)
       self.courseB = Course.objects.create(courseName='B', courseDescription='test', courseID=2, courseSemester=self.semester2)
       self.sectionA = Section.objects.create(sectionID=1, type="Lecture", course=self.courseA, taID=self.user)
       self.sectionB = Section.objects.create(sectionID=2, type="Lab", course=self.courseB, taID=self.user)

    def test_noInput(self):
        self.assertFalse(self.section.createSection(), "No inputs, course should not have been created.")
    def test_preExists(self):
        self.assertFalse(self.section.createSection(1, "Lecture", self.courseA), "Section already exists.")
        self.assertFalse(self.section.createSection(2, "Lab", self.courseB), "Section already exists.")
    def test_sameID(self):
        self.assertFalse(self.section.createSection(1, "Lecture", self.courseB), "SectionID already used. Invalid")
        self.assertFalse(self.section.createSection(2, "Lab", self.courseA), "SectionID already used. Invalid.")
    def test_diffName(self):
        self.assertTrue(self.section.createSection(3, "Lecture", self.courseA, self.user), "Different name. Valid")
        self.assertTrue(self.section.createSection(4, "Lab", self.courseB, self.user), "Different name. Valid")
    def test_invalidType(self):
        self.assertFalse(self.section.createSection(3, "Class", self.courseA), "Invalid Section type.")
class testSectionDeletion(TestCase):
    def setUp(self):
        self.section = SectionClass()
        self.course = CourseClass()
        self.role = Roles.TA
        self.user = User.objects.create(userID='testuser', password='testpass', email='test@test.com',
                                        phone='1234567890',
                                        address='testaddress', role=self.role, firstName='testfirst',
                                        lastName='testlast')
        self.season = Seasons.Fall
        self.semester1 = Semester.objects.create(season=self.season, year=2024)
        self.semester2 = Semester.objects.create(season=self.season, year=2025)
        self.courseA = Course.objects.create(courseName='A', courseDescription='test', courseID=1,
                                             courseSemester=self.semester1)
        self.courseB = Course.objects.create(courseName='B', courseDescription='test', courseID=2,
                                             courseSemester=self.semester2)
        self.sectionA = Section.objects.create(sectionID=1, type="Lecture", course=self.courseA, taID=self.user)
        self.sectionB = Section.objects.create(sectionID=2, type="Lab", course=self.courseB, taID=self.user)

    def test_noInput(self):
        self.assertFalse(self.section.deleteSection(), "No section was chosen for deletion")
    def test_deleteNonexistant(self):
        self.assertFalse(self.section.deleteSection(3), "Section does not exist to be deleted")
    def test_deleteExistant(self):
        self.assertTrue(self.section.deleteSection(self.sectionA.sectionID), "Section exists to be deleted")
class testViewCourses(TestCase):
    def setUp(self):
        self.section = SectionClass()
        self.course = CourseClass()
        self.role = Roles.TA
        self.user = User.objects.create(userID='testuser', password='testpass', email='test@test.com',
                                        phone='1234567890',
                                        address='testaddress', role=self.role, firstName='testfirst',
                                        lastName='testlast')
        self.season = Seasons.Fall
        self.semester1 = Semester.objects.create(season=self.season, year=2024)
        self.semester2 = Semester.objects.create(season=self.season, year=2025)
        self.courseA = Course.objects.create(courseName='A', courseDescription='test', courseID=1,
                                             courseSemester=self.semester1)
        self.courseB = Course.objects.create(courseName='B', courseDescription='test', courseID=2,
                                             courseSemester=self.semester2)
        self.sectionA = Section.objects.create(sectionID=1, type="Lecture", course=self.courseA, taID=self.user)
        self.sectionB = Section.objects.create(sectionID=2, type="Lab", course=self.courseB, taID=self.user)
    def test_noInput(self):
        with self.assertRaises(ValueError):
            self.section.viewSection()
    def test_viewExistant(self):
        self.assertEqual(self.section.viewSection(self.sectionA.sectionID), "1" " Lecture" " 1")
        self.assertEqual(self.section.viewSection(self.sectionB.sectionID), "2" " Lab" " 2")
    def test_viewNonexistant(self):
        with self.assertRaises(ValueError):
            self.section.viewSection(3)
class testEditSection(TestCase):
    def setUp(self):
        self.course = CourseClass()
        self.role = Roles.TA
        self.user1 = User.objects.create(userID='testuser1', password='testpass1', email='test1@test.com',
                                        phone='1234567890',
                                        address='testaddress1', role=self.role, firstName='testfirst1',
                                        lastName='testlast1')
        self.user2 = User.objects.create(userID='testuser2', password='testpass2', email='test2@test.com',
                                        phone='1234567891',
                                        address='testaddress2', role=self.role, firstName='testfirst2',
                                        lastName='testlast2')
        self.season = Seasons.Fall
        self.semester1 = Semester.objects.create(season=self.season, year=2024)
        self.semester2 = Semester.objects.create(season=self.season, year=2025)
        self.courseA = Course.objects.create(courseName='A', courseDescription='test', courseID=1,
                                             courseSemester=self.semester1)
        self.courseB = Course.objects.create(courseName='B', courseDescription='test', courseID=2,
                                             courseSemester=self.semester2)
        self.sectionA = Section.objects.create(sectionID=1, type="Lecture", course=self.courseA, taID=self.user1)
        self.sectionB = Section.objects.create(sectionID=2, type="Lab", course=self.courseB, taID=self.user2)
        self.section = SectionClass()
    def test_noInput(self):
        with self.assertRaises(AttributeError):
            self.sectionA.editSection(self.sectionA, random_attribute='value')
    def test_editType(self):
        self.assertTrue(self.section.editSection(self.sectionA, type='Lab'), "Section type should be changed")
        self.assertEqual(Section.objects.get(sectionID=self.sectionA.sectionID).type, 'Lab')
        self.assertEqual(Section.objects.get(sectionID=self.sectionA.sectionID).taID, self.user1)
    def test_editUser(self):
        self.assertTrue(self.section.editSection(self.sectionA, taID=self.user2),
                        "User should be changed")
        self.assertEqual(Section.objects.get(sectionID=self.sectionA.sectionID).taID, self.user2)
        self.assertEqual(Section.objects.get(sectionID=self.sectionA.sectionID).type, "Lecture")
    def test_editBoth(self):
        self.assertTrue(self.section.editSection(self.sectionA, type='Lab', taID=self.user2),
                        "Both fields should be changed")
        self.assertEqual(Section.objects.get(sectionID=self.sectionA.sectionID).type, "Lab")
        self.assertEqual(Section.objects.get(sectionID=self.sectionA.sectionID).taID, self.user2)
class testSectInDB(TestCase):
    def setUp(self):
        self.section = SectionClass()
        self.course = CourseClass()
        self.role = Roles.TA
        self.user = User.objects.create(userID='testuser', password='testpass', email='test@test.com',
                                        phone='1234567890',
                                        address='testaddress', role=self.role, firstName='testfirst',
                                        lastName='testlast')
        self.season = Seasons.Fall
        self.semester1 = Semester.objects.create(season=self.season, year=2024)
        self.semester2 = Semester.objects.create(season=self.season, year=2025)
        self.courseA = Course.objects.create(courseName='A', courseDescription='test', courseID=1,
                                             courseSemester=self.semester1)
        self.courseB = Course.objects.create(courseName='B', courseDescription='test', courseID=2,
                                             courseSemester=self.semester2)
        self.sectionA = Section.objects.create(sectionID=1, type="Lecture", course=self.courseA, taID=self.user)
        self.sectionB = Section.objects.create(sectionID=2, type="Lab", course=self.courseB, taID=self.user)
    def test_noInput(self):
        self.assertFalse(self.section.sectInDB(), "No section was chosen to check.")
    def test_sectExists(self):
        self.assertTrue(self.section.sectInDB(self.sectionA.sectionID), "Section exists to check.")
    def test_sectNotExists(self):
        self.assertFalse(self.section.sectInDB(3), "Section does not exist.")




if __name__ == '__main__':
    unittest.main()
