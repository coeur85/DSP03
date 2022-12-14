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

    def __ValidateGradeAddRemove(self, studentId, courseId):
        student = self.__Students.SelectStudent(studentId)
        if student == None:
            raise RuntimeError('invaled studet id')
        course = self.__Courses.SelectCourse(courseId)
        if course == None:
            raise RuntimeError('invalied course id')

    def StudentsAddNew(self, name: str):
        try:
            self.__Students.AddNewStudent(name)
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def StudentsDelete(self, Id):
        try:
            self.__Students.DeleteStudent(Id)
            courseIdToDelete = 1
            while courseIdToDelete <= self.__CourseSize:
                self.GradeTryToRemove(Id, courseIdToDelete)
                courseIdToDelete += 1
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def StudentsUpdate(self, Id, Name):
        try:
            self.__Students.UpdateStudent(Id, Name)
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def StudnetsPrint(self):
        self.__Students.PrintAll()

    def CourseAddNew(self, name: str):
        try:
            self.__Courses.AddNewCourse(name)
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def CourseDelete(self, Id):
        try:
            self.__Courses.DeleteCourse(Id)
            studentIdToDelete = 1
            while studentIdToDelete <= self.__StudentSize:
                self.GradeTryToRemove(studentIdToDelete, Id)
                studentIdToDelete += 1
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def CourseUpdate(self, Id, name):
        try:
            self.__Courses.UpdateCourse(Id, name)
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def CoursesPrint(self):
        self.__Courses.PrintAll()

    def GradeAddNew(self, studentId, courseId, grade):
        try:
            self.__ValidateGradeAddRemove(studentId, courseId)
            self.__Grades.AddCourseToStudent(studentId, courseId, grade)
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def GradeRemove(self, studentId, courseId):
        try:
            self.__ValidateGradeAddRemove(studentId, courseId)
            self.GradeTryToRemove(studentId, courseId)
            self.__saveAll()
        except Exception as ex:
            print(ex)

    def GradeTryToRemove(self, studentId, courseId):
        try:
            self.__Grades.RemoveCourseFromStudent(studentId, courseId)
        except Exception as ex:
            print(ex)

    def GradesForStudent(self, studentId):
        student = self.__Students.SelectStudent(studentId)
        gradesList = self.__Grades.SelectStudentCouresList(studentId)
        print(student)
        if len(gradesList) > 0:
            print('----his/her course list-----')
            for grade in gradesList:
                course = self.__Courses.SelectCourse(grade.CourseId)
                print(f'{course}, his/her scoore: {grade.Grade}')
        print(f'---- end of report with {len(gradesList)} course')

    def GradeForCourse(self, courseId):
        course = self.__Courses.SelectCourse(courseId)
        gradesList = self.__Grades.SelectCoureStudentList(courseId)
        print(course)
        if len(gradesList) > 0:
            print('----its student list-----')
            for grade in gradesList:
                course = self.__Students.SelectStudent(grade.StudentId)
                print(f'{course}, his/her scoore: {grade.Grade}')
        print(f'---- end of report with {len(gradesList)} student')
