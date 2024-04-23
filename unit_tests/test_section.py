from classes.section import SectionClass
from classes.courseClass import CourseClass
from project_app.models import Section, Course
from django.test import TestCase
import unittest

class testCreateSection(TestCase):

    def setUp(self):
       self.section = SectionClass("","","")
       self.course = CourseClass()
       self.courseA = self.course.createCourse(name="A", semester="Fall 2024", courseID=1, description="")
       self.courseB = self.course.createCourse(name="B", semester="Fall 2024", courseID=2, description="")
       self.sectionA = Section.objects.create(sectionID = 3, sectionType="Lecture", courseID=self.courseA)
       self.sectionB = Section.objects.create(sectionID = 4, sectionType="Lab", courseID=self.courseB)

    def test_noInput(self):
        self.assertFalse(self.section.createSection("","",""), "No inputs, course should not have been created.")
    def test_preExists(self):
        self.assertFalse(self.section.createSection(3, "Lecture", self.courseA), "Section already exists.")
        self.assertFalse(self.section.createSection(4, "Lab", self.courseB), "Section already exists.")
    def test_nonexistantCourse(self):
        self.assertFalse(self.section.createSection(3, "Lecture", 3), "CourseID does not exist.")
        self.assertFalse(self.section.createSection(4, "Lab", 4), "CourseID does not exist.")
    def test_diffCourse(self):
        self.assertTrue(self.section.createSection(3, "Lecture", "2"), "Different course. Valid.")
        self.assertTrue(self.section.createSection(4, "Lab", "1"), "Different course. Valid.")
        courseA_List = Section.objects.filter(courseID="1")
        courseB_List = Section.objects.filter(courseID="2")
        self.assertEqual(len(courseA_List), 2)
        self.assertEqual(len(courseB_List), 2)
    def test_diffName(self):
        self.assertTrue(self.section.createSection(4, "Lecture", "1"), "Different name. Valid")
    def test_diffType(self):
        self.assertTrue(self.section.createSection(3, "Lab", "1"), "Different type. Valid")
    def test_invalidType(self):
        self.assertFalse(self.section.createSection(4, "Class", "1"), "Invalid Section type.")
class testSectionDeletion(TestCase):
    def setUp(self):
        self.section = SectionClass("", "", "")
        self.course = CourseClass()
        self.courseA = self.course.createCourse(name="A", semester="Fall 2024", courseID=1, description="")
        self.courseB = self.course.createCourse(name="B", semester="Fall 2024", courseID=2, description="")
        self.sectionA = Section.objects.create(sectionID="A", sectionType="Lecture", courseID=self.courseA)
        self.sectionB = Section.objects.create(sectionID="B", sectionType="Lab", courseID=self.courseB)

    def test_noInput(self):
        self.assertFalse(self.section.deleteSection(), "No section was chosen for deletion")
    def test_deleteNonexistant(self):
        self.assertFalse(self.section.deleteSection("C"), "Section does not exist to be deleted")
    def test_deleteExistant(self):
        self.assertTrue(self.section.deleteSection("A"), "Section exists to be deleted")
class testViewCourses(TestCase):
    def setUp(self):
        self.section = SectionClass("", "", "")
        self.course = CourseClass()
        self.courseA = self.course.createCourse(name="A", semester="Fall 2024", courseID=1, description="")
        self.courseB = self.course.createCourse(name="B", semester="Fall 2024", courseID=2, description="")
        self.sectionA = Section.objects.create(sectionID="A", sectionType="Lecture", courseID=self.courseA)
        self.sectionB = Section.objects.create(sectionID="B", sectionType="Lab", courseID=self.courseB)
    def test_noInput(self):
        with self.assertRaises(ValueError):
            self.section.viewSection()
    def test_viewExistant(self):
        self.assertEqual(self.section.viewSection("A"), "A" "Lecture" "1")
        self.assertEqual(self.section.viewSection("B"), "B" "Lab" "2")
    def test_viewNonexistant(self):
        with self.assertRaises(ValueError):
            self.section.viewSection("C")
class testSectInDB(TestCase):
    def setUp(self):
        self.section = SectionClass("", "", "")
        self.course = CourseClass()
        self.courseA = self.course.createCourse(name="A", semester="Fall 2024", courseID=1, description="")
        self.courseB = self.course.createCourse(name="B", semester="Fall 2024", courseID=2, description="")
        self.sectionA = Section.objects.create(sectionID="A", sectionType="Lecture", courseID=self.courseA)
        self.sectionB = Section.objects.create(sectionID="B", sectionType="Lab", courseID=self.courseB)
    def test_noInput(self):
        self.assertFalse(self.section.sectInDB(), "No section was chosen to check.")
    def test_sectExists(self):
        self.assertTrue(self.section.sectInDB("A"), "Section exists to check.")
    def test_sectNotExists(self):
        self.assertFalse(self.section.sectInDB("C"), "Section does not exist.")




if __name__ == '__main__':
    unittest.main()
