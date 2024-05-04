from project_app.models import Assignment, Course,User

class AssignmentClass:

    def assignUser(self, userID="", courseID=0):

        if (courseID == 0 or (not Course.objects.filter(courseID=courseID).exists()) or
                (not User.objects.filter(userID=userID).exists())):
            return False
        course = Course.objects.get(courseID=courseID)
        user = User.objects.get(userID=userID)
        if (Assignment.objects.filter(userID=user, courseID=course).exists() or user.role == "Admin"):
            return False

        Assignment.objects.create(userID=user, courseID=course)
        return True

