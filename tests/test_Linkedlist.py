import unittest
from DataStructure.LinkedList import LinkedList
from Models.Student import Student


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.studentsList = LinkedList()
        # add basic data
        self.student1 = Student(1, 'ahmed')
        self.student2 = Student(1, 'eman')
        self.studentsList.Add(self.student1)
        self.studentsList.Add(self.student2)

    def test_AddStudent(self):
        # gevin
        studentToAdd = Student(3, 'TestStudent')
        # when
        self.studentsList.Add(studentToAdd)
        retrevedStudent = self.studentsList.Select(3)
        # then
        self.assertEqual(self.studentsList.lenth(), 3)
        self.assertEqual(retrevedStudent, studentToAdd)
