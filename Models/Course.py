class Course:
    def __init__(self,id, name):
        self.Id = id
        self.Name = name
    def __str__(self) -> str:
        return f'course with id:{self.Id}, name:{self.Name}'