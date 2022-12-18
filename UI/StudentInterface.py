from rich.prompt import Prompt
from Context.Context import Context
class StudentInterface():
    def __init__(self,promot : Prompt,context : Context):
        self.promote = promot
        self.context = context


    def AddNewStudent(self):
        studentName = self.promote.ask('enter student name')
        self.context.StudentsAddNew(studentName)
