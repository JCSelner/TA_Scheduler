from project_app.models import Section, Course, User

class SectionClass:
    def __init__(self, sectionID=0, sectionType="Lab", course=Course(), taID=User()):
        self.sectionID = sectionID
        self.sectionType = sectionType
        self.course=course
        self.taID=taID
    def sectInDB(self, sectionID=""):
        sectionList = Section.objects.filter(sectionID=sectionID)
        return len(sectionList)==1
    def createSection(self, sectionID="", sectionType="", course=Course(), taID=None):
        #Check for a unique sectionID
        if self.sectInDB(sectionID) or sectionID=="":
            return False
        #Check for valid section type
        if sectionType != "Lab" and sectionType != "Lecture":
            return False
        Section.objects.create(sectionID=sectionID, type=sectionType, course=course, taID=taID)
        return True
    def editSection(self, sectionID="", type=None, taID=None):
        if not self.sectInDB(sectionID):
            return False
        section = Section.objects.get(sectionID=sectionID)
        if type is None and taID is None:
            return False
        if type is not None:
            section.type = type
        if taID is not None:
            section.taID = taID
        section.save()
        return True
    def deleteSection(self, sectionID=""):
        if not self.sectInDB(sectionID):
            return False
        Section.objects.filter(sectionID=sectionID).delete()
        return True

    def viewSection(self, sectionID=""):
        if not self.sectInDB(sectionID):
            raise ValueError
        sectionList = Section.objects.filter(sectionID=sectionID)
        section_view = sectionList[0]
        return section_view.sectionID + " " + section_view.type + " " + section_view.course.courseID.__str__()
