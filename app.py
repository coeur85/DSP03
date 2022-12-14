from DataStructure.LinkedList import LinkedList
from Models.Student import Student


strudent1 = Student("ahmed")
strudent2 = Student("israa")
strudent3 = Student("mohamed")

studentLinkedList = LinkedList()

studentLinkedList.AddHead(strudent1)
studentLinkedList.AddHead(strudent2)
studentLinkedList.AddHead(strudent3)

studentLinkedList.print()

studentLinkedList.RemoveValue(strudent2)
studentLinkedList.print()
