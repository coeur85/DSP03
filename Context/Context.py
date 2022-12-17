from DataStructure.HashTable import HashTbale
from DataStructure.LinkedList import LinkedList
from Models.Course import Course
from Models.Student import Student
from Models.StudentCourse import StudentCourse
from Storage.Broker.StorageBroker import StorageBroker


class Context():
    def __init__(self):
        StudentSize = 10
        CourseSize = 10
        self._studentContext = self.Students()
        self._courseContext = self.Courses()
        self._studentCourseContext = self.StudentCourse(
            StudentSize * CourseSize)

    class Students():
        def __init__(self):
            self._studentList = LinkedList()
            self._currentMaxStudentId = 1
            self.studentsFileName = 'students'
            self.storage = StorageBroker()
            newObject = self.storage.LoadFromFile(self.studentsFileName)
            if newObject != None:
                self = newObject

        def AddNewStudent(self, name):
            newStudent = Student(self._currentMaxStudentId, name)
            self._studentList.Add(newStudent)
            self._currentMaxStudentId += 1
            self.storage.SaveToFile(self.studentsFileName, self)

    class Courses():
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

    class StudentCourse():
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
