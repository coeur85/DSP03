from DataStructure.LinkedList import LinkedList
from DataStructure.LinkedList2D import LinkedList2D
from Models.Student import Student
from Models.Course import Course


strudent1 = Student("ahmed")
strudent2 = Student("israa")
strudent3 = Student("mohamed")

course1 = Course('arabic')
course2 = Course('math')
course3 = Course('since')

# studentLinkedList = LinkedList()

# studentLinkedList.AddHead(strudent1)
# studentLinkedList.AddHead(strudent3)

# studentLinkedList.print()

# studentLinkedList.RemoveValue(strudent2)
# studentLinkedList.print()

studentsCourses = LinkedList2D()

studentsCourses.AddStudentToCourse(10, course1, strudent1)
studentsCourses.AddStudentToCourse(9, course1, strudent2)
studentsCourses.AddStudentToCourse(8, course1, strudent3)

studentsCourses.AddStudentToCourse(101, course2, strudent1)
studentsCourses.AddStudentToCourse(109, course2, strudent2)
studentsCourses.AddStudentToCourse(108, course2, strudent3)


studentsCourses.printAll()
