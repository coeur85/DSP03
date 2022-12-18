from Context.Context import Context

context = Context()


context.StudentsAddNew('ahmed')     # 1
context.StudentsAddNew('mohamed')   # 2
context.StudentsAddNew('eman')      # 3
context.StudentsAddNew('sarah')     # 4
context.StudentsAddNew('esraa')     # 5


context.CourseAddNew('math')        # 1
context.CourseAddNew('arabic')      # 2
context.CourseAddNew('german')      # 3
context.CourseAddNew('spanish')     # 4
context.CourseAddNew('russin')      # 5

# student 1
context.GradeAddNew(1, 1, 10)
context.GradeAddNew(1, 2, 11)
context.GradeAddNew(1, 3, 12)

# student 2
context.GradeAddNew(2, 3, 13)
context.GradeAddNew(2, 4, 14)

# student 3
context.GradeAddNew(3, 4, 15)
context.GradeAddNew(3, 5, 16)
# student 4
context.GradeAddNew(4, 5, 17)
# student 5
context.GradeAddNew(5, 1, 18)
context.GradeAddNew(5, 2, 19)
context.GradeAddNew(5, 3, 20)
context.GradeAddNew(5, 4, 21)
context.GradeAddNew(5, 5, 22)
