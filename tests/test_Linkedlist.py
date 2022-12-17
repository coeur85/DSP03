import unittest
from DataStructure.LinkedList import LinkedList
from Models.Student import Student


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.studentsList = LinkedList()
        # add basic data
        student1 = Student(1, 'ahmed')
        student2 = Student(2, 'eman')
        self.studentsList.Add(student1)
        self.studentsList.Add(student2)

    def GetNewRandomStudent(self) -> Student:
        return Student(3, 'TestStudent')

    def GetExistingStudent(self) -> Student:
        return Student(1, 'ahmed')


class TestAdd(TestLinkedList):
    def test_ShouldAddStudent(self):
        # gevin
        studentToAdd = self.GetNewRandomStudent()
        # when
        self.studentsList.Add(studentToAdd)
        retrevedStudent = self.studentsList.Select(studentToAdd.Id)
        # then
        self.assertEqual(self.studentsList.lenth(), 3)
        self.assertEqual(retrevedStudent, studentToAdd)

    def test_ShouldThrowsExceptionIfStudentAlreadyExists(self):
        # gevin
        studentToAdd = self.GetExistingStudent()
        # when
        # then
        with self.assertRaises(Exception) as context:
            self.studentsList.Add(studentToAdd)


class TestRemove(TestLinkedList):
    def test_ShouldRemoveStudent(self):
        # gevin
        studentToAdd = self.GetNewRandomStudent()
        stuentToRemove = studentToAdd
        self.studentsList.Add(studentToAdd)
        # when
        self.studentsList.Remove(stuentToRemove.Id)
        # then
        self.assertEqual(self.studentsList.lenth(), 2)

    def test_ShouldThrowExptionIfStudentDoesNotExisits(self):
        # gevin
        studentToRemnove = self.GetNewRandomStudent()
        # when
        # then
        with self.assertRaises(Exception) as context:
            self.studentsList.Remove(studentToRemnove.Id)

    def test_ShouldThrowExceptionIfListIsEmpty(self):
        # gevin
        emptyList = LinkedList()
        # when
        # then
        with self.assertRaises(Exception) as context:
            emptyList.Remove(1)


class TestSelect(TestLinkedList):
    def test_ShouldSelectStudent(self):
        # gevin
        expectedStudent = self.GetExistingStudent()
        # when
        retrviedStudent = self.studentsList.Select(expectedStudent.Id)
        # then
        self.assertEqual(expectedStudent, retrviedStudent)

    def test_ShouldReturnNoneIfStudentDoesNotExisit(self):
        # gevin
        newStudent = self.GetNewRandomStudent()
        # when
        retrivedStudent = self.studentsList.Select(newStudent.Id)
        # then
        self.assertIsNone(retrivedStudent)

    def test_ShouldReturnNoneIfListIsEmpty(self):
        # gevin
        newList = LinkedList()
        # when
        retrivedStudent = newList.Select(1)
        # then
        self.assertIsNone(retrivedStudent)


class TestUpdate(TestLinkedList):
    def test_ShouldUpdate(self):
        # gevin
        orginalStudent = self.GetExistingStudent()
        newName = 'Omar'
        expectedUpdatedStudent = orginalStudent
        expectedUpdatedStudent.Name = newName
        # when
        dbStudent = self.studentsList.Select(orginalStudent.Id)
        dbStudent.Name = newName
        self.studentsList.Update(dbStudent.Id, dbStudent)
        updatedStudent = self.studentsList.Select(orginalStudent.Id)
        # then
        self.assertEqual(expectedUpdatedStudent, updatedStudent)

    def test_ShouldReturnNoneIfStudentDoesNotExisit(self):
        # gevin
        newStudent = self.GetNewRandomStudent()
        # when
        # then
        with self.assertRaises(Exception) as _:
            self.studentsList.Update(newStudent.Id, newStudent)
