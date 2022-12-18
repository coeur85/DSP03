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
        self._studentContext = self.StudentContext()
        self._courseContext = self.CourseContext()
        self._studentCourseContext = self.StudentCourseContext(
            StudentSize * CourseSize)

    class StudentCourseContext():
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

    class StudentContext(StudentCourseContext):
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

        def DeleteStudent(self, Id: int):
            self._studentList.Remove(Id)
            self.storage.SaveToFile(self.studentsFileName, self)
            courseIdToDelete = Id * 10
            while courseIdToDelete < ((Id * 10) - 1):
                self.RemoveCourseFromStudent(Id, courseIdToDelete)
                courseIdToDelete += 1

    class CourseContext(StudentCourseContext):
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
            studentIdToDelete = 1
            while studentIdToDelete < (len(self._gradesTable.size)):
                self.RemoveCourseFromStudent(studentIdToDelete,Id)
                studentIdToDelete += 10
