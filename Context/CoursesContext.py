
from DataStructure.LinkedList import LinkedList
from Models.Course import Course
from Storage.Broker.StorageBroker import StorageBroker


class CourseContext():
    def __init__(self):
        self._courseList = LinkedList()
        self._currentMaxCourseId = 1
        self.courseFileName = 'courses'
        self.storage = StorageBroker()
        newObject = self.storage.LoadFromFile(self.courseFileName)
        if newObject != None:
            self = newObject

    def AddNewCourse(self, name):
        newCourse = Course(self._currentMaxCourseId, name)
        self._courseList.Add(newCourse)
        self._currentMaxCourseId += 1
        self.storage.SaveToFile(self.courseFileName, self)

    def DeleteCourse(self, Id):
        self._courseList.Remove(Id)
        self.storage.SaveToFile(self.courseFileName, self)
