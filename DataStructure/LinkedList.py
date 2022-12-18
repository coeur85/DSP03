class LinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.next = next
            self.value = value

    def __init__(self):
        self.head = None
        self.size = 0

    def __keyExists(self, key) -> bool:
        current = self.head
        while current != None:
            if current.value.Id != key:
                current = current.next
            else:
                return True
        return False

    def lenth(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def Add(self, value):
        if self.__keyExists(value.Id):
            raise RuntimeError('this key already exists, key:', value.Id)
        newNode = self.Node(value, self.head)
        self.head = newNode
        self.size += 1

    def Remove(self, key):
        if self.isEmpty():
            raise RuntimeError("list is empty")
        if self.__keyExists(key) == False:
            raise RuntimeError("item with key:", key, "was not found")
        if self.head.value.Id == key:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next != None:
            if current.next.value.Id == key:
                current.next = current.next.next
                self.size -= 1
                return True
            else:
                current = current.next

    def Select(self, key):
        current = self.head
        if current == None:
            return None
        if self.head.value.Id == key:
            return self.head.value
        while current.next != None:
            if current.next.value.Id != key:
                current = current.next
            else:
                return current.next.value
        return None

    def Update(self, key, value):
        current = self.head
        if current == None:
            raise RuntimeError('data list is empty, nothing to update')
        if self.__keyExists(key) == False:
            raise RuntimeError("item with key:", key, "was not found")
        if self.head.value.Id == key:
            self.head.value = value
            return True
        while current.next != None:
            if current.next.value.Id != key:
                current = current.next
            else:
                current.next.value = value
                return True
        return False

    def Print(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print(f'-----------------------')
        print(f'total {self.size} items')
        print(f'-----------------------')
