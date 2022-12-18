class Course:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name

    def __str__(self) -> str:
        return f'course with id:{self.Id}, name:{self.Name}'

    def __eq__(self, other) -> bool:
       if other == None and self.Id == 0 and len(self.name) ==0 :
            return True
       elif other == None :
            return False
       else :
            return self.Id == other.Id and self.Name == other.Name

    def __repr__(self):
        return f"course (id={repr(self.Id)}, name={repr(self.Name)})"
