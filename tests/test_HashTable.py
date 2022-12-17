import unittest
from DataStructure.HashTable import HashTbale
from Models.Student import Student


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.arr_size = 10
        self.dataTable = HashTbale(self.arr_size)
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

    def test_ShouldThrowExceptionIfKeyLessthan1(self):
        # gevin
        invaledStudent = Student(-1, 'ahmed')
        # when
        # then
        with self.assertRaises(Exception) as _:
            self.dataTable.Add(invaledStudent.Id, invaledStudent)

    def test_ShouldThrowExceptionIfKeyBiggerThantableSize(self):
        # gevin
        invaledStudent = Student(self.arr_size + 1, 'ahmed')
        # when
        # then
        with self.assertRaises(Exception) as _:
            self.dataTable.Add(invaledStudent.Id, invaledStudent)

    def test_ShouldThrowExceptionIfStudentAlreadyExisits(self):
        # gevin
        invaledStudent = self.GetExistingStudent()
        # when
        # then
        with self.assertRaises(Exception) as _:
            self.dataTable.Add(invaledStudent.Id, invaledStudent)


class TestRemove(TestHashTable):
    def test_ShouldRemoveStudent(self):
        # gevin
        exisitingStudent = self.GetExistingStudent()
        # when
        self.dataTable.Remove(exisitingStudent.Id)
        dbStudent = self.dataTable.Select(exisitingStudent.Id)
        # then
        self.assertIsNone(dbStudent)

    def test_ShouldThrowErrorIfStudentAlreadyRemoved(self):
        # gevin
        exisitingStudent = self.GetExistingStudent()
        self.dataTable.Remove(exisitingStudent.Id)
        # when
        # then
        with self.assertRaises(Exception) as _:
            self.dataTable.Remove(exisitingStudent.Id)


class TestSelect(TestHashTable):
    def test_ShouldSelect(self):
        # gevin
        exisitingStudent = self.GetExistingStudent()
        # when
        retrivedStudent = self.dataTable.Select(exisitingStudent.Id)
        # then
        self.assertEqual(exisitingStudent, retrivedStudent)

    def test_ShouldRetrunNoneIfStudentDoesNotExisits(self):
        # gevin
        newStudent = self.GetNewRandomStudent()
        # when
        retrivedStudent = self.dataTable.Select(newStudent.Id)
        # then
        self.assertIsNone(retrivedStudent)


class TestUpdate(TestHashTable):
    def test_ShouldUpdate(self):
        # gvin
        exisitingStudent = self.GetExistingStudent()
        newName = 'Omar'
        expectedUpdatedStudent = exisitingStudent
        expectedUpdatedStudent.Name = newName
        exisitingStudent.Name = newName
        # when
        self.dataTable.Update(exisitingStudent.Id, exisitingStudent)
        updatedStudent = self.dataTable.Select(exisitingStudent.Id)
        # then
        self.assertEqual(expectedUpdatedStudent, updatedStudent)
    def test_ShouldThrowErrorIfKeyDoesNotExisits(self):
        # gvin
        newStudent = self.GetNewRandomStudent()
        # when
        # then
        with self.assertRaises(Exception) as _:
            self.dataTable.Update(newStudent.Id,newStudent)
