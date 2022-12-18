from Context.CoursesContext import CourseContext
from Context.StudentsContext import StudentContext
from Context.GradesContext import GradesContext
from Storage.Broker.StorageBroker import StorageBroker


class Context():
    def __init__(self):
        self.__StudentSize = 10
        self.__CourseSize = 10
        self.__Students = StudentContext()
        self.__Courses = CourseContext()
        self.__Grades = GradesContext(self.__StudentSize, self.__CourseSize)
        self.storage = StorageBroker()
        self.courseFileName = 'courses'
        self.studentsFileName = 'students'
        self.gradeFileName = 'grades'
        self.storage = StorageBroker()

        newObject = self.storage.LoadFromFile(self.studentsFileName)
        if newObject != None:
            self.__Students = newObject
        newObject = self.storage.LoadFromFile(self.courseFileName)
        if newObject != None:
            self.__Courses = newObject
        newObject = self.storage.LoadFromFile(self.gradeFileName)
        if newObject != None:
            self.__Grades = newObject

    def __saveAll(self):
        self.storage.SaveToFile(self.studentsFileName, self.__Students)
        self.storage.SaveToFile(self.courseFileName, self.__Courses)
        self.storage.SaveToFile(self.gradeFileName, self.__Grades)

    def StudentsAddNew(self, name: str):
        self.__Students.AddNewStudent(name)
        self.__saveAll()

    def StudentsDelete(self, Id):
        self.__Students.DeleteStudent(Id)
        courseIdToDelete = 1
        while courseIdToDelete <= self.__CourseSize:
            self.GradeRemove(Id, courseIdToDelete)
            courseIdToDelete += 1
        self.__saveAll()

    def StudnetsPrint(self):
        self.__Students.PrintAll()

    def CourseAddNew(self, name: str):
        self.__Courses.AddNewCourse(name)
        self.__saveAll()

    def CourseDelete(self, Id):
        self.__Courses.DeleteCourse(Id)
        studentIdToDelete = 1
        while studentIdToDelete <= self.__StudentSize:
            self.GradeRemove(studentIdToDelete, Id)
            studentIdToDelete += 1
        self.__saveAll()

    def CoursesPrint(self):
        self.__Courses.PrintAll()

    def GradeAddNew(self, studentId, courseId, grade):
        self.__Grades.AddCourseToStudent(studentId, courseId, grade)
        self.__saveAll()

    def GradeRemove(self, studentId, courseId):
        self.__Grades.RemoveCourseFromStudent(studentId, courseId)
        self.__saveAll()

    def GradeStudentGrades(self, studentId):
        student = self.__Students.SelectStudent(studentId)
        gradesList = self.__Grades.PrintStudentCoures(studentId)
        print(student)
        print('----his/her course list-----')
        for grade in gradesList :
            course = self.__Courses.SelectCourse(grade.CourseId)
            print(f'{course}, his/her scoore: {grade.Grade}')
        print(f'---- end of report with {len(gradesList)} recoreds')
