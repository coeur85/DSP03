class LinkedList2D:
    class Node2D:
        def __init__(self, grade, student, course, nextStudent=None, nextCourse=None):
            self.Grade = grade
            self.Student = student
            self.Course = course
            self.NextStudentNode = nextStudent
            self.NextCourseNode = nextCourse

    def __init__(self):
        self.studentSize = 0
        self.courseSzie = 0
        self.studentHead = None
        self.courseHead = None
