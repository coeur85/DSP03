
from DataStructure.LinkedList import LinkedList
from Models.Course import Course



class CourseContext():
    def __init__(self):
        self._courseList = LinkedList()
        self._currentMaxCourseId = 1
       
    def AddNewCourse(self, name):
        newCourse = Course(self._currentMaxCourseId, name)
        self._courseList.Add(newCourse)
        self._currentMaxCourseId += 1

    def DeleteCourse(self, Id):
        self._courseList.Remove(Id)
