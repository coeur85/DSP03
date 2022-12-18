from DataStructure.LinkedList import LinkedList
from Models.Student import Student


class StudentContext():
    def __init__(self):
        self._studentList = LinkedList()
        self._currentMaxStudentId = 1

    def AddNewStudent(self, name):
        newStudent = Student(self._currentMaxStudentId, name)
        self._studentList.Add(newStudent)
        self._currentMaxStudentId += 1

    def DeleteStudent(self, Id: int):
        self._studentList.Remove(Id)

    def PrintAll(self):
        print(f'---- Students list ----')
        self._studentList.Print()

    def SelectStudent(self, studentId):
        student = self._studentList.Select(studentId)
        return student

    def UpdateStudent(self, key, name):
        dbStudent = self._studentList.Select(key)
        dbStudent.Name = name
        self._studentList.Update(key, dbStudent)
