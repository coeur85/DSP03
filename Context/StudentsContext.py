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