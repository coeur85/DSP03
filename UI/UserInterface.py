from rich.prompt import Prompt


class UserInterface():
    add: str = 'add'
    remove: str = 'remove'
    update: str = 'update'
    report: str = 'report'

    student: str = 'student'
    course: str = 'course'
    grade: str = 'grade'

    back: str = 'back'

    def HomePage(self):
        choices = [self.add, self.remove, self.update, self.report]
        response = Prompt.ask("What do u wich to do ?", choices=choices)
        match response:
            case self.add:
                self.AddPage()
            case self.remove:
                self.RemovePage()
            case self.Update:
                self.UpdatePage()
            case self.report:
                self.ReportPage()

    def AddPage(self):
        choices = [self.student, self.course, self.grade, self.back]
        response = Prompt.ask("What do you want to add ?", choices=choices)
        match response:
            case self.back:
                self.HomePage()

    def RemovePage(self):
        choices = ["Student", "Course", 'Grade', '<-- Back']
        response = Prompt.ask("What do you want to delete ?",
                              choices=choices, show_choices=True)

    def UpdatePage(self):
        choices = ["Student", "Course", '<-- Back']
        response = Prompt.ask("What do you want to add ?",
                              choices=choices, show_choices=True)

    def ReportPage(self):
        choices = ["All Students", "All Courses", 'Spasfic student course',
                   'Spasfic course studnets', '<-- Back']
        response = Prompt.ask("What do you want to add ?",
                              choices=choices, show_choices=True)
