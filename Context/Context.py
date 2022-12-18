from Context.CoursesContext import CourseContext
from Context.StudentsContext import StudentContext
from Context.GradesContext import GradesContext


class Context():
    def __init__(self):
        StudentSize = 10
        CourseSize = 10
        self.__Students = StudentContext()
        self.__Courses = CourseContext()
        self.__Grades = GradesContext(StudentSize * CourseSize)

    def StudentsAddNew(self, name: str):
        self.__Students.AddNewStudent(name)

    def StudentsDelete(self, Id):
        self.__Students.Remove(Id)
        courseIdToDelete = Id * 10
        while courseIdToDelete < ((Id * 10) - 1):
            self.RemoveCourseFromStudent(Id, courseIdToDelete)
            courseIdToDelete += 1

    def CourseAddNew(self, name: str):
        self.__Courses.AddNewCourse(name)

    def CourseDelete(self, Id):
        self.__Courses.Remove(Id)
        studentIdToDelete = 1
        while studentIdToDelete < (len(self._gradesTable.size)):
            self.RemoveCourseFromStudent(studentIdToDelete, Id)
            studentIdToDelete += 10

    def GradeAddNew(self, studentId, courseId, grade):
        self.__Grades.AddCourseToStudent(studentId, courseId, grade)

    def GradeRemove(self, studentId, courseId):
        self.__Grades.RemoveCourseFromStudent(studentId, courseId)
