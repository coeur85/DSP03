from rich.prompt import *
from Context.Context import Context


class StudentInterface():
    def __init__(self, promot: Prompt, context: Context):
        self.promote = promot
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
    def PrintAllStudents(self):
        self.context.StudnetsPrint()
    def 