from django.test import TestCase
from project_app.models import Assignment, Semester, User
from classes import courseClass, assignmentClass

class TestAssignUser(TestCase):

    def setUp(self):
        self.ta = User.objects.create(userID="TA", password="TA", email="blank@gmail.com", phone=0, firstName="T", lastName="A", role="TA", address="None")
        self.instructor = User.objects.create(userID="Instruct", password="Instructor", email="blank2@gmail.com", phone=0, firstName="In", lastName="Struct", role="Instructor", address="None")
        self.admin = User.objects.create(userID="Admin", password="Admin", email="blank3@gmail.com", phone=0, firstName="Ad",lastName="Min", role="Admin", address="None")
        courseClass.CourseClass.createCourse(courseClass.CourseClass,"Test Course", Semester.objects.create(), 7357)
        courseClass.CourseClass.createCourse(courseClass.CourseClass, "Test Course2", Semester.objects.create(), 0)
        self.assignment = assignmentClass.AssignmentClass
        Assignment.objects.create(userID="TA",courseID=0)


    def test_noInput(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass),"assignment should not be empty")

    def test_nonexistantClass(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "TA", 1), "assignment should have a class in the database")

    def test_nonexistantUser(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "none", 7357), "assignment should have a user in the database")

    def test_duplicateAssignment(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "TA", 0), "There should not be any duplicate assignments")

    def test_assignAdmin(self):
        self.assertFalse(self.assignment.assignUser(assignmentClass.AssignmentClass, "Admin", 7357), "assigning of admin should not be allowed")

    def test_assignTA(self):
        self.assertTrue(self.assignment.assignUser(assignmentClass.AssignmentClass, "TA", 7357), "assigning of TA should be allowed")
        assignments = Assignment.objects.all()
        self.assertEquals(len(assignments), 2)

    def test_assignInstructor(self):
        self.assertTrue(self.assignment.assignUser(assignmentClass.AssignmentClass, "Instruct", 7357), "assigning of Instructor should be allowed")
        assignments = Assignment.objects.all()
        self.assertEquals(len(assignments), 2)
