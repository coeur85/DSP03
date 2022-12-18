from DataStructure.HashTable import HashTbale
from Models.Grade import Grade


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

    def SelectStudentCouresList(self, studentId) -> list:
        courseIdToSelect = 1
        outputList = list()
        while courseIdToSelect <= (self.__courseSize):
            searchKey = self.__computeKey(studentId,courseIdToSelect)
            grade = self._gradesTable.Select(searchKey)
            if grade != None:
                if grade.StudentId == studentId:
                    outputList.append(grade)
            courseIdToSelect += 1
        return outputList

    def SelectCoureStudentList(self, courseId) -> list:
        studentIdToSelect = 1
        outputList = list()
        while studentIdToSelect <= (self.__studentSize):
            searchKey = self.__computeKey(studentIdToSelect,courseId)
            grade = self._gradesTable.Select(searchKey)
            if grade != None:
                if grade.CourseId == courseId:
                    outputList.append(grade)
            studentIdToSelect += 1
        return outputList
