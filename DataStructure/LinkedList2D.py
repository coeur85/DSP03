class LinkedList2D:
    class Node2D:
        def __init__(self, value, student, course, nextStudent=None, nextCourse=None):
            self.Grade = value
            self.Student = student
            self.Course = course
            self.NextStudentNode = nextStudent
            self.NextCourseNode = nextCourse

    def __init__(self):
        self.studentSize = 0
        self.courseSzie = 0
        self.studentHead = None
        self.courseHead = None

    def AddStudentToCourse(self, grade, course, student):
        
        

    def printAll(self):
        print('starting from students')
        currentStudent = self.studentHead
        while currentStudent != None:
            print('stdent name', currentStudent.Student.Name,
                  ' --- current course:', currentStudent.Course.Name, ' --- Grade:', currentStudent.Grade)
            currentStudent = currentStudent.NextStudentNode
        print('-------------------------')
        print('starting from course list')
        currentCourse = self.courseHead
        while currentCourse != None:
            print('course name', currentCourse.Course.Name,
                  ' --- current student:', currentCourse.Student.Name, ' --- Grade:', currentCourse.Grade)
            currentCourse = currentCourse.NextCourseNode
        print('end of printing')

    def printForStudent(self, printSudent):
        currentStudentNode = self.studentHead
        while currentStudentNode != None:
            if (currentStudentNode.Student != printSudent):
                currentStudentNode = currentStudentNode.NextStudentNode
            else:
                break
        print('printing courses for student :',
              currentStudentNode.Student.Name)
        studentCourse = currentStudentNode.Course
        print('course name:', studentCourse.Name)
        currentCourseNode = currentStudentNode.NextCourseNode
        while currentCourseNode != None:
            print('course: ', currentCourseNode.course.Name)
            currentCourseNode = currentCourseNode.NextCourseNode
