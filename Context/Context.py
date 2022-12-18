from Context.CoursesContext import CourseContext
from Context.StudentsContext import StudentContext
from Context.GradesContext import GradesContext


class Context():
    def __init__(self):
        StudentSize = 10
        CourseSize = 10
        self.Students = StudentContext()
        self.Courses = CourseContext()
        self.Grades = GradesContext(StudentSize * CourseSize)

    def StudentsAddNew(self, name: str):
        self.Students.AddNewStudent(name)

    def StudentsDelete(self, Id):
        self.Students.Remove(Id)
        courseIdToDelete = Id * 10
        while courseIdToDelete < ((Id * 10) - 1):
            self.RemoveCourseFromStudent(Id, courseIdToDelete)
            courseIdToDelete += 1

    def CourseAddNew(self, name: str):
        self.Courses.AddNewCourse(name)

    def CourseDelete(self, Id):
        self.Courses.Remove(Id)
        studentIdToDelete = 1
        while studentIdToDelete < (len(self._gradesTable.size)):
            self.RemoveCourseFromStudent(studentIdToDelete, Id)
            studentIdToDelete += 10

    def GradeAddNew(self, studentId, courseId, grade):
        self.Grades.AddCourseToStudent(studentId, courseId, grade)

    def GradeRemove(self, studentId, courseId):
        self.Grades.RemoveCourseFromStudent(studentId, courseId)
