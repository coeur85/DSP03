import unittest
from DataStructure.HashTable import HashTbale
from Models.Student import Student


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.dataTable = HashTbale(10)
        # add basic data
        student1 = Student(1, 'ahmed')
        student2 = Student(2, 'eman')
        student3 = Student(3, 'esraa')
        student4 = Student(4, 'mohamed')
        student5 = Student(5, 'ebrahem')
        self.dataTable.Add(student1.Id, student1)
        self.dataTable.Add(student2.Id, student2)
        self.dataTable.Add(student3.Id, student3)
        self.dataTable.Add(student4.Id, student4)
        self.dataTable.Add(student5.Id, student5)

    def GetNewRandomStudent(self) -> Student:
        return Student(6, 'TestStudent')

    def GetExistingStudent(self) -> Student:
        return Student(1, 'ahmed')


class TestAdd(TestHashTable):
    def test_ShouldAddStudent(self):
        # gevin
        studentToAdd = self.GetNewRandomStudent()
        # when
        self.dataTable.Add(studentToAdd.Id, studentToAdd)
        retrivedStudent = self.dataTable.Select(studentToAdd.Id)
        # then
        self.assertEqual(retrivedStudent, studentToAdd)
