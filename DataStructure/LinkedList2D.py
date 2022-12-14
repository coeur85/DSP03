class LinkedList2D:
    class Node2D:
        def __init__(self, value, student, course, nextStudent=None, nextCourse=None):
            self.value = value
            self.student = student
            self.course = course
            self.NextStudent = nextStudent
            self.NextCourse = nextCourse

    def __init__(self):
        self.studentSize = 0
        self.courseSzie = 0
        self.studentHead = None
        self.courseHead = None

    def AddStudentToCourse(self, grade, course, student):
        newNode = self.Node2D(grade, student, course,
                              self.studentHead, self.courseHead)

        currentCourse = self.courseHead
        while currentCourse
