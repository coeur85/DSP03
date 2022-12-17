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

    def GetRandomStudent(self) -> Student:
        return Student(3, 'TestStudent')

    def test_AddStudent(self):
        # gevin
        studentToAdd = self.GetRandomStudent()
        # when
        self.studentsList.Add(studentToAdd)
        retrevedStudent = self.studentsList.Select(studentToAdd.Id)
        # then
        self.assertEqual(self.studentsList.lenth(), 3)
        self.assertEqual(retrevedStudent, studentToAdd)
    def test_AddStudentAlreadyExists(self):
        # gevin
        studentToAdd = Student(1,'adam')
        # when
        # then
        self.assertRaises(Exception,self.studentsList.Add(studentToAdd))

    def test_RemoveStudent(self):
        # gevin
        studentToAdd = self.GetRandomStudent()
        stuentToRemove = studentToAdd
        self.studentsList.Add(studentToAdd)
        # when
        self.studentsList.Remove(stuentToRemove.Id)
        # then
        self.assertEqual(self.studentsList.lenth(), 2)

    def test_RemoveDoesNotExisitsStudnet(self):
        # gevin
        studentToRemnove = self.GetRandomStudent()
        # when
        # then
        self.assertRaises(
            Exception, self.studentsList.Remove(studentToRemnove.Id))
