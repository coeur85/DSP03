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
        self.courseHead = newNode
        self.studentHead = newNode

    def printAll(self):
        print('starting from students')
        currentStudent = self.studentHead
        while currentStudent != None:
            print('stdent name', currentStudent.student.Name,
                  ' --- current course:', currentStudent.course.Name, ' --- Grade:', currentStudent.value)
            currentStudent = currentStudent.NextStudent
        print('-------------------------')
        print('starting from course list')
        currentCourse = self.courseHead
        while currentCourse != None:
            print('course name', currentCourse.course.Name,
                  ' --- current student:', currentCourse.student.Name, ' --- Grade:', currentCourse.value)
            currentCourse = currentCourse.NextCourse
        print('end of printing')
