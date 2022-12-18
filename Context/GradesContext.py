from DataStructure.HashTable import HashTbale
from Models.StudentCourse import Grade


class GradesContext():
    def __init__(self, studentSize, coursesize):
        self.__studentSize = studentSize
        self.__courseSize = coursesize
        self._gradesTable = HashTbale(studentSize * coursesize)
        self.studentCourseFielName = 'grades'

    def __computeKey(self, studentId: int, courseId: int) -> int:
        newStudentId = studentId - 1
        newCourseId = courseId - 1
        stringNewId = f'{newStudentId}{newCourseId}'
        newKey = int(stringNewId) + 1
        return newKey

    def AddCourseToStudent(self, studentId, courseId, grade):
        key = self.__computeKey(studentId, courseId)
        newStudentCourse = Grade(studentId, courseId, grade)
        self._gradesTable.Add(key, newStudentCourse)

    def RemoveCourseFromStudent(self, studentId, courseId):
        key = self.__computeKey(studentId, courseId)
        self._gradesTable.Remove(key)

    def PrintStudentCoures(self, studentId) -> list:
        i = 1
        outputList = list()
        while i <= (self.__studentSize * self.__courseSize):
            grade = self._gradesTable.Select(i)
            if grade != None:
                if grade.StudentId == studentId:
                    outputList.append(grade)
            i += 1
        return outputList
