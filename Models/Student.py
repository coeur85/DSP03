class Student:
    Id: int
    Name: str

    def __init__(self, id, name):
        self.Id = id
        self.Name = name

    def __str__(self) -> str:
        return f'student with id:{self.Id}, name:{self.Name}'

    def __eq__(self, other) -> bool:
        return self.Id == other.Id and self.Name == other.Name

    def __repr__(self):
        return f"student (id={repr(self.Id)}, name={repr(self.Name)})"
