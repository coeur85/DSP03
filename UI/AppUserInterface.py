from UI.StudentInterface import StudentInterface
from UI.CourseInterface import CourseInterface
from rich.prompt import Prompt
from Context.Context import Context


class AppUserInterface():
    add: str = 'add'
    remove: str = 'remove'
    update: str = 'update'
    reportAll: str = 'showAll'
    reportOne: str = 'showOne'
    addGrade: str = 'addGrade'
    removeGrade: str = 'removeGrade'

    student: str = 'student'
    course: str = 'course'

    back: str = 'back'

    def __init__(self):
        self.context = Context()
        self.studentInterface = StudentInterface(self.context)
        self.courseInterface = CourseInterface(self.context)

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
                   self.reportAll, self.reportOne, self.addGrade, self.removeGrade, self.back]
        response = Prompt.ask(
            "What do u wish to do with students?", choices=choices)
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
            case self.addGrade:
                self.studentInterface.AddGradeForStudent()
            case self.removeGrade:
                self.studentInterface.RemoveGradeFormStudent()
            case self.back:
                self.HomePage()
        self.StudentsPage()

    def CoursePage(self):
        choices = [self.add, self.remove, self.update,
                   self.reportAll, self.reportOne, self.addGrade, self.removeGrade, self.back]
        response = Prompt.ask(
            "What do u what wish to do with courses?", choices=choices)
        match response:
            case self.add:
                self.courseInterface.AddNewCourse()
            case self.remove:
                self.courseInterface.DeleteCourse()
            case self.update:
                self.courseInterface.UpdateCourse()
            case self.reportAll:
                self.courseInterface.PrintAllCourses()
            case self.reportOne:
                self.courseInterface.PrintCourseCourses()
            case self.addGrade:
                self.courseInterface.AddGradeForCourse()
            case self.removeGrade:
                self.courseInterface.RemoveGradeFormCourse()
            case self.back:
                self.HomePage()
        self.CoursePage()
