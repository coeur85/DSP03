from UI.StudentInterface import StudentInterface
from UI.StudentInterface import CourseInterface
from rich.prompt import Prompt
from Context.Context import Context


class AppUserInterface():
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
                   self.reportAll, self.reportOne, self.addgrade, self.back]
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
            case self.addgrade:
                self.studentInterface.AddGradeForStudent()
            case self.back:
                self.HomePage()
        self.StudentsPage()

    def CoiursesPage(self):
        choices = [self.add, self.remove, self.update,
                   self.reportAll, self.reportOne, self.addgrade, self.back]
        response = Prompt.ask(
            "What do u what wish to do with students?", choices=choices)
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
            case self.addgrade:
                self.courseInterface.AddGradeForCourse()
            case self.back:
                self.HomePage()
        self.CoiursesPage()
