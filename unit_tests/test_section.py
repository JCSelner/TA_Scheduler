from classes.section import SectionClass
from project_app.models import Section, Course
from django.test import TestCase
import unittest

class testCreateSection(TestCase):

    def setup(self):
       self.section = SectionClass()
       self.sectionA = Section.objects.create(sectionID = "A", sectionType="Lecture", courseID="1")

    def test_noInput(self):
        self.assertFalse(self.section.createSection(), "No inputs, course should not have been created.")
    def test_preExists(self):
        self.assertFalse(self.section.createSection("A", "Lecture", "1"), "Course already exists.")
    def test_diffCourse(self):
        self.assertTrue(self.section.createSection("A", "Lecture", "2"), "Different course. Valid.")
    def test_diffName(self):
        self.assertTrue(self.section.createSection("B", "Lecture", "1"), "Different name. Valid")
    def test_diffType(self):
        self.assertTrue(self.section.createSection("A", "Lab", "1"), "Different type. Valid")
    def test_invalidType(self):
        self.assertFalse(self.section.createSection("B", "Lab", "1"), "Invalid type. Valid")



if __name__ == '__main__':
    unittest.main()
