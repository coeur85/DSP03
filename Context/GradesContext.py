from DataStructure.HashTable import HashTbale
from Models.StudentCourse import StudentCourse



class GradesContext():
    def __init__(self, studentSize,coursesize):
        self.__studentSize = studentSize
        self.__courseSize = coursesize
        self._gradesTable = HashTbale(studentSize * coursesize)
        self.studentCourseFielName = 'grades'

    def __computeKey(self, studentId: int, courseId: int) -> int:
        if courseId == self.__courseSize: # last key of the arry
            return (studentId + 1) * self.__courseSize 
        newKey = f'{studentId}{courseId}'
        return int(newKey)

    def AddCourseToStudent(self, studentId, courseId, grade):
        key = self.__computeKey(studentId, courseId)
        newStudentCourse = StudentCourse(studentId, courseId, grade)
        self._gradesTable.Add(key, newStudentCourse)

    def RemoveCourseFromStudent(self, studentId, courseId):
        key = self.__computeKey(studentId, courseId)
        self._gradesTable.Remove(key)
