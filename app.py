from Context.Context import Context

context = Context()

# context.Students.AddNewStudent(context._studentContext, 'ahmed')
# context.SaveToFile()

context.LoadFromFile()

context.Students.AddNewStudent(context._studentContext, 'ahmed')
