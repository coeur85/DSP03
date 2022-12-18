from DataStructure.HashTable import HashTbale
from Models.StudentCourse import StudentCourse
from Storage.Broker.StorageBroker import StorageBroker


class GradesContext():
    def __init__(self, tableSize):
        self._gradesTable = HashTbale(tableSize)
        self.studentCourseFielName = 'studentCourse'
        self.storage = StorageBroker()
        newObject = self.storage.LoadFromFile(self.studentCourseFielName)
        if newObject != None:
            self = newObject

    def __computeKey(self, studentId: int, courseId: int) -> int:
        newKey = f'{studentId}{courseId}'
        return int(newKey)

    def AddCourseToStudent(self, studentId, courseId, grade):
        key = self.__computeKey(studentId, courseId)
        newStudentCourse = StudentCourse(studentId, courseId, grade)
        self._gradesTable.Add(key, newStudentCourse)
        self.storage.SaveToFile(self.studentCourseFielName, self)

    def RemoveCourseFromStudent(self, studentId, courseId):
        key = self.__computeKey(studentId, courseId)
        self._gradesTable.Remove(key)
        self.storage.SaveToFile(self.studentCourseFielName, self)
