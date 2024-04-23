from project_app.models import Section, Course

class SectionClass:
    def __init__(self, sectionID, sectionType):
        self.sectionID = sectionID
        self.sectionType = sectionType
    def sectInDB(self, sectionID):
        sectionList = Section.objects.filter(sectionID=sectionID)
        return len(sectionList)==1
    def createSection(self, sectionID, sectionType, course):
        if self.sectInDB(sectionID):
            return False
        sectionList = Section.objects.filter(sectionID=sectionID, sectionType=sectionType, courseID=course)
        if len(sectionList)!=0:
            return False

        Section.objects.create(sectionID=sectionID, sectionType=sectionType, courseID=course)
        if sectionType != "Lab" and sectionType != "Lecture":
            return False
        return True

    def deleteSection(self, sectionID):
        if (not self.sectInDB(sectionID)):
            return False
        Course.objects.filter(sectionID=sectionID).delete()
        return True

    def viewSection(self, sectionID):
        if (not self.sectInDB(sectionID)):
            return False
        sectionList = Section.objects.filter(sectionID=sectionID)
        section_view = sectionList[0]
        return section_view.sectionID + " " + section_view.sectionType + " " + section_view.course.courseID
