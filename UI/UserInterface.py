from UI import StudentInterface
from rich.prompt import Prompt
from Context.Context import Context


class UserInterface():
    add: str = 'add'
    remove: str = 'remove'
    update: str = 'update'
    reportAll: str = 'showAll'
    reportOne: str = 'showOne'
    addgrade: str = 'addGrade'

    student: str = 'student'
    course: str = 'course'
    grade: str = 'grade'

    back: str = 'back'

    def __init__(self):
        self.context = Context()
        self.studentInterface = StudentInterface(self.context)

    def HomePage(self):
        choices = [self.student, self.course]
        response = Prompt.ask("What do u wish to work on ?", choices=choices)
        match response:
            case self.student:
                self.StudentsPage()
            case self.course:
                self.CoursePage()

    def StudentsPage(self):
        choices = [self.add, self.remove, self.update,
                   self.reportAll, self.reportOne, self.addgrade, self.back]
        response = Prompt.ask(
            "What do u what to do with students?", choices=choices)
        match response:
            case self.add:
                self.studentInterface.AddNewStudent()
            case self.remove:
                self.studentInterface.DeleteStudent()
            case self.update:
                self.studentInterface.UpdateStudent()
            case self.reportAll:
                self.studentInterface.PrintAllStudents()
            case self.reportOne:
                self.studentInterface.PrintStudentCourses()
            case self.addgrade:
                self.studentInterface.AddGradeForStudent()
            case self.back:
                self.HomePage()
