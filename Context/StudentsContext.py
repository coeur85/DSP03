from DataStructure.LinkedList import LinkedList
from Models.Student import Student
from Storage.Broker.StorageBroker import StorageBroker


class StudentContext():
    def __init__(self):
        self._studentList = LinkedList()
        self._currentMaxStudentId = 1
        self.studentsFileName = 'students'
        self.storage = StorageBroker()
        newObject = self.storage.LoadFromFile(self.studentsFileName)
        if newObject != None:
            self = newObject

    def AddNewStudent(self, name):
        newStudent = Student(self._currentMaxStudentId, name)
        self._studentList.Add(newStudent)
        self._currentMaxStudentId += 1
        self.storage.SaveToFile(self.studentsFileName, self)

    def DeleteStudent(self, Id: int):
        self._studentList.Remove(Id)
        self.storage.SaveToFile(self.studentsFileName, self)