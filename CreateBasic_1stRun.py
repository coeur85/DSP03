from Context.Context import Context

context = Context()


context.StudentContext.AddNewStudent(context._studentContext, 'ahmed')  # 1
context.StudentContext.AddNewStudent(context._studentContext, 'mohamed')  # 2
context.StudentContext.AddNewStudent(context._studentContext, 'eman')  # 3
context.StudentContext.AddNewStudent(context._studentContext, 'sarah')  # 4
context.StudentContext.AddNewStudent(context._studentContext, 'esraa')  # 5


context.CourseContext.AddNewCourse(context._courseContext, 'math')  # 1
context.CourseContext.AddNewCourse(context._courseContext, 'arabic')  # 2
context.CourseContext.AddNewCourse(context._courseContext, 'german')  # 3
context.CourseContext.AddNewCourse(context._courseContext, 'spanish')  # 4
context.CourseContext.AddNewCourse(context._courseContext, 'russin')  # 5

# student 1
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 1, 1, 10)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 1, 2, 11)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 1, 3, 12)

# student 2
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 2, 3, 13)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 2, 4, 14)

# student 3
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 3, 4, 15)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 3, 5, 16)
# student 4
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 4, 5, 17)
# student 5
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 5, 1, 18)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 5, 2, 19)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 5, 3, 20)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 5, 4, 21)
context.StudentCourseContext.AddCourseToStudent(
    context._studentCourseContext, 5, 5, 22)
