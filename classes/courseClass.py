from project_app.models import Course


class CourseClass:

    def isInDB(self, courseID):
        coursesList = Course.objects.filter(courseID=courseID)
        return len(coursesList) == 1

    def createCourse(self, name, semester, courseID, description=""):
        if (self.isInDB(courseID)):
            return False

        coursesList = Course.objects.filter(courseName=name, courseSemester=semester)
        if (len(coursesList) != 0):
            return False

        Course.objects.create(courseName= name, courseSemester=semester, courseID= courseID, courseDescription=description)

        return True

    def deleteCourse(self, courseID):
        if (not self.isInDB(courseID)):
            return False
        # delete course of that type
        Course.objects.filter(courseID=courseID).delete()
        return True

    def viewCourse(self, courseID):
        if (not self.isInDB(courseID)):
            raise ValueError
        coursesList = Course.objects.filter(courseID=courseID)
        that = coursesList[0]
        return that.courseName + " " + that.courseSemester + " " + that.courseDescription
