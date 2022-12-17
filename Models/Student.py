class Student:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name

    def __str__(self) -> str:
        return f'student with id:{self.Id}, name:{self.Name}'
