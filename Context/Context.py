from DataStructure.HashTable import HashTbale
from DataStructure.LinkedList import LinkedList
from Models.Course import Course
from Models.Student import Student


class Context:
    def __init__(self, studentSize, courseSize):
        self.StudentSize = studentSize
        self.CourseSize = courseSize

    class Students():
        def __init__(self):
            self.studentList = LinkedList()
            self.currentMaxStudentId = 1

        def AddNewStudent(self, name):
            newStudent = Student(self.currentMaxStudentId, name)
            self.studentList.Add(newStudent)
            self.currentMaxStudentId += 1

    class Courses():
        def __init__(self):
            self.courseList = LinkedList()
            self.currentMaxCourseId = 1

        def AddNewCourse(self, name):
            newCourse = Course(self.currentMaxCourseId, name)
            self.courseList.Add(newCourse)
            self.currentMaxCourseId += 1

      