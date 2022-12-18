class Grade:
    StudentId: int
    CourseId: int
    Grade: int

    def __init__(self, studentId, courseId, grade):
        self.StudentId = studentId
        self.CourseId = courseId
        self.Grade = grade

    def __str__(self) -> str:
        return f'Greade :{self.Grade}'
