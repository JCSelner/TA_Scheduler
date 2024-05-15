from project_app.models import Section, Course, User


class SectionClass:
    def __init__(self, sectionID=0, type="Lab", course=Course(), taID=User()):
        self.sectionID = sectionID
        self.type = type
        self.course = course
        self.taID = taID

    def sectInDB(self, sectionID=0):
        sectionList = Section.objects.filter(sectionID=sectionID)
        return len(sectionList) == 1

    def createSection(self, sectionID=0, type="", course=Course(), taID=None):
        # Check for a unique sectionID
        if self.sectInDB(self, sectionID) or sectionID == 0:
            return False
        # Check for valid section type
        if type != "Lab" and type != "Lecture":
            return False
        Section.objects.create(sectionID=sectionID, type=type, course=course, taID=taID)
        return True

    def editSection(self, section, **kwargs):
        for key, value in kwargs.items():
            if hasattr(Section, key):
                setattr(section, key, value)
            else:
                raise AttributeError(f"Attribute '{key}' does not exist in Section")
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
