from django.test import TestCase
from project_app.models import Assignment, Semester, User
from classes import courseClass, assignmentClass, accounts
from unittest.mock import Mock
class TestAssignUser(TestCase):

    def setUp(self):
        self.ta = User.objects.create(userID="TA", password="TA", email="blank@gmail.com", phone=0, firstName="T", lastName="A", role="TA", address="None")
        self.instructor = User.objects.create(userID="Instruct", password="Instructor", email="blank2@gmail.com", phone=0, firstName="In", lastName="Struct", role="Instructor", address="None")
        self.admin = User.objects.create(userID="Admin", password="Admin", email="blank3@gmail.com", phone=0, firstName="Ad",lastName="Min", role="Admin", address="None")
        self.ta.save()
        self.instructor.save()
        self.admin.save()
        courseClass.CourseClass.createCourse(courseClass.CourseClass,"Test Course", Semester.objects.create(), 7357)
        self.assignment = assignmentClass.AssignmentClass

    def test_noInput(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass))

    def test_nonexistantClass(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "TA", 1))

    def test_nonexistantUser(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "none", 7357))

    def test_assignAdmin(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "Admin", 7357))

    def test_assignTA(self):
        self.assertTrue(self.assignment.assignUser(assignmentClass.AssignmentClass, "TA", 7357))
        assignments = Assignment.objects.all()
        self.assertEquals(len(assignments), 1)

    def test_assignInstructor(self):
        self.assertTrue(self.assignment.assignUser(assignmentClass.AssignmentClass, "Instruct", 7357))
        assignments = Assignment.objects.all()
        self.assertEquals(len(assignments), 1)
