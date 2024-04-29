from classes.courseClass import CourseClass
from project_app.models import Course, Semester, Seasons
from django.test import TestCase


class TestCreateCourse(TestCase):

    def setUp(self):
        self.course = CourseClass()
        self.fall = Seasons.Fall
        self.currentYear = 2024
        self.semester = Semester.objects.create(season=self.fall, year=self.currentYear, semesterID=0)
        self.diffSemester = Semester.objects.create(season=self.fall, year=2028, semesterID=0)
        self.negSemester = Semester.objects.create(season=self.fall, year=-2029, semesterID=0)
        self.math101 = Course.objects.create(courseName="Math 101", courseSemester=self.semester, courseID=123)

    def test_noInput(self):
        self.assertFalse(self.course.createCourse(), "Course should not be created")

    def test_addCourseIDAlreadyInDB(self):
        self.assertFalse(self.course.createCourse("Math 101",  self.semester, 123),
                         "Allows adding of an existing courseID")

    def test_addCourseNameAlreadyInDB(self):
        self.assertFalse(self.course.createCourse("Math 101", self.semester, 456),
                         "Allows adding of an existing course name")

    def test_differentSemesterSameName(self):
        self.assertTrue(self.course.createCourse("Math 101", self.diffSemester, 456), "Not allows adding different semester")
        coursesList = Course.objects.all()
        self.assertEqual(len(coursesList), 2)
        # test if added

    def test_differentNameSameSemester(self):
        self.assertTrue(self.course.createCourse("Math 102",  self.semester, 456), "Not allow adding of different name")
        coursesList = Course.objects.all()
        self.assertEqual(len(coursesList), 2)

    def test_differentEverything(self):
        self.assertTrue(self.course.createCourse("Math 102",  self.diffSemester, 456), "Not allows adding different everything")
        coursesList = Course.objects.all()
        self.assertEqual(len(coursesList), 2)

    def test_negativeSemester(self):
        self.assertFalse(self.course.createCourse("Math 102", self.negSemester, 456),"Allows negative semester")


class TestDeleteCourse(TestCase):

    def setUp(self):
        self.course = CourseClass()
        self.fall = Seasons.Fall
        self.semester = Semester.objects.create(season=self.fall, year=2024, semesterID=0)
        self.math101 = Course.objects.create(courseName="Math 101", courseSemester=self.semester, courseID=123)

    def test_noInput(self):
        self.assertFalse(self.course.deleteCourse(), "Allows deletion of an Non-existing courseID")

    def test_deleteNonexistant(self):
        self.assertFalse(self.course.deleteCourse(456), "Allows deletion of an Non-existing courseID")

    def test_deleteExistant(self):
        self.assertTrue(self.course.deleteCourse(123), "Not allows deletion of an Existing courseID")
        coursesList = Course.objects.all()
        self.assertEqual(len(coursesList), 0)


class TestViewCourses(TestCase):
    def setUp(self):
        self.course = CourseClass()
        self.fall = Seasons.Fall
        self.semester = Semester.objects.create(season=self.fall, year=2024, semesterID=0)
        self.math101 = Course.objects.create(courseName="Math 101", courseSemester=self.semester, courseID=123)

    def test_noInput(self):
        with self.assertRaises(ValueError):
            self.course.viewCourse()

    def test_viewExistant(self):
        self.assertEqual(self.course.viewCourse(123), "Math 101 Fall 2024 ", self.course.viewCourse(123))

    def test_viewNonExistant(self):
        with self.assertRaises(ValueError):
            self.course.viewCourse(456)


class TestIsInDB(TestCase):
    def setUp(self):
        self.course = CourseClass()
        self.fall = Seasons.Fall
        self.semester = Semester.objects.create(season=self.fall, year=2024, semesterID=0)
        self.math101 = Course.objects.create(courseName="Math 101", courseSemester=self.semester, courseID=123)


    def test_noInput(self):
        self.assertFalse(self.course.isInDB())

    def test_existant(self):
        self.assertTrue(self.course.isInDB(123))

    def test_nonExistant(self):
        self.assertFalse(self.course.isInDB(456))