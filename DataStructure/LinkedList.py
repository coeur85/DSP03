class LinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.next = next
            self.value = value

    def __init__(self):
        self.head = None
        self.size = 0

    def lenth(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def AddHead(self, value):
        newNode = self.Node(value, self.head)
        self.head = newNode
        self.size += 1

    def RemoveValue(self, value):
        if self.isEmpty():
            raise RuntimeError("list is empty")
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next != None:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return True
            else:
                current = current.next
        raise RuntimeError("item with value:", value, "was not found")

    def print(self):
        current = self.head
        print('---- list size :', self.size, ' ----')
        while current != None:
            print(current.value.Name)
            current = current.next
        print('---- end of list ----')
