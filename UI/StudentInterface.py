from rich.prompt import *
from Context.Context import Context


class StudentInterface():
    def __init__(self, context: Context):
        self.context = context

    def AddNewStudent(self):
        studentName = Prompt.ask('enter student name')
        self.context.StudentsAddNew(studentName)

    def DeleteStudent(self):
        studentId = IntPrompt.ask('enter student Id')
        self.context.StudentsDelete(studentId)

    def UpdateStudent(self):
        studentId = IntPrompt.ask('enter student Id')
        studentName = Prompt.ask('enter student new name')
        self.context.StudentsUpdate(studentId, studentName)

    def PrintAllStudents(self):
        self.context.StudnetsPrint()

    def PrintStudentCourses(self):
        studentId = IntPrompt.ask('enter student Id')
        self.context.GradesForStudent(studentId)

    def AddGradeForStudent(self):
        studentId = IntPrompt.ask('enter student Id')
        courseId = IntPrompt.ask('enter course Id')
        grade = IntPrompt.ask('enter student grade scoor for this course')
        self.context.GradeAddNew(studentId, courseId, grade)

    def RemoveGradeFormStudent(self):
        studentId = IntPrompt.ask('enter student Id')
        courseId = IntPrompt.ask('enter course Id')
        self.context.GradeRemove(studentId, courseId)
