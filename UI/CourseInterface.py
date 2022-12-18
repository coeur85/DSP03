from rich.prompt import *
from Context.Context import Context


class CourseInterface():
    def __init__(self, context: Context):
        self.context = context

    def AddNewCourse(self):
        courseName = Prompt.ask('enter Course name')
        self.context.CourseAddNew(courseName)

    def DeleteCourse(self):
        courseId = IntPrompt.ask('enter Course Id')
        self.context.CourseDelete(courseId)

    def UpdateCourse(self):
        courseId = IntPrompt.ask('enter Course Id')
        courseName = Prompt.ask('enter Course new name')
        self.context.CourseUpdate(courseId, courseName)

    def PrintAllCourses(self):
        self.context.CoursesPrint()

    def PrintCourseCourses(self):
        courseId = IntPrompt.ask('enter Course Id')
        self.context.GradeForCourse(courseId)

    def AddGradeForCourse(self):
        courseId = IntPrompt.ask('enter Course Id')
        studentId = IntPrompt.ask('enter student Id')
        grade = IntPrompt.ask('enter Course grade scoor for this student')
        self.context.GradeAddNew(studentId, courseId,  grade)
