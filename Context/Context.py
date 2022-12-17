import pickle

from DataStructure.HashTable import HashTbale
from DataStructure.LinkedList import LinkedList
from Models.Course import Course
from Models.Student import Student
from Models.StudentCourse import StudentCourse


class Context(Course, Student):
    def __init__(self):
        StudentSize = 10
        CourseSize = 10
        self._studentContext = self.Students()
        self.Courses()
        self.StudentCourse(StudentSize * CourseSize)

    def __SaveToFile(self, fileName: str, objectToSave):
        with open(f'Data/{fileName}.dbfile', 'wb') as contextFile:
            pickle.dump(objectToSave, contextFile)

    def __LoadFromFile(self, fileName: str, objectToLoad):
        with open(f'Data/{fileName}.dbfile', 'rb') as contextFile:
            objectToLoad = pickle.load(contextFile)

    class Students():
        def __init__(self):
            self._studentList = LinkedList()
            self._currentMaxStudentId = 1
            studentsFileName = 'students'

        def AddNewStudent(self, name):
            newStudent = Student(self._currentMaxStudentId, name)
            self._studentList.Add(newStudent)
            self._currentMaxStudentId += 1

    class Courses():
        def __init__(self):
            self._courseList = LinkedList()
            self._currentMaxCourseId = 1

        def AddNewCourse(self, name):
            newCourse = Course(self._currentMaxCourseId, name)
            self._courseList.Add(newCourse)
            self._currentMaxCourseId += 1

    class StudentCourse():
        def __init__(self, tableSize):
            self._gradesTable = HashTbale(tableSize)

        def __computeKey(self, studentId: int, courseId: int) -> int:
            newKey = f'{studentId}{courseId}'
            return int(newKey)

        def AddCourseToStudent(self, studentId, courseId, grade):
            key = self.__computeKey(studentId, courseId)
            newStudentCourse = StudentCourse(studentId, courseId, grade)
            self._gradesTable.Add(key, newStudentCourse)
