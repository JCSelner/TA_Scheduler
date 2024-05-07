from project_app.models import Course, Semester, Seasons


class CourseClass:

    def __init__(self, courseName="", description="", courseID=0, semester=Semester()):
        self.courseName = courseName
        self.description = description
        self.courseID = courseID
        self.semester = semester

    def isInDB(self, courseID = 0):
        coursesList = Course.objects.filter(courseID=courseID)

        return len(coursesList) == 1

    def createCourse(self, name="", semester=Semester(), courseID=0, description=""):
        if(self.isInDB(courseID) or courseID == 0):
            return False

        if(Course.objects.filter(courseName=name, courseSemester=semester).exists()):
            return False
        if(semester == None or semester.year < 0):
            return False

        Course.objects.create(courseName= name, courseSemester=semester, courseID=courseID, courseDescription=description)

        return True

    def deleteCourse(self, courseID=0):
        if (not self.isInDB(courseID)):
            return False
        # delete course of that type
        Course.objects.filter(courseID=courseID).delete()
        return True

    def viewCourse(self, courseID=0):
        if (not self.isInDB(courseID)):
            raise ValueError
        coursesList = Course.objects.filter(courseID=courseID)
        that = coursesList[0]
        return that.courseName + " " + that.courseSemester.__str__() + " " + that.courseDescription
