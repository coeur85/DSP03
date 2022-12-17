from Context.Context import Context

context = Context()


context.Students.AddNewStudent(context._studentContext, 'ahmed')        #1
context.Students.AddNewStudent(context._studentContext, 'mohamed')      #2
context.Students.AddNewStudent(context._studentContext, 'eman')         #3
context.Students.AddNewStudent(context._studentContext, 'sarah')        #4
context.Students.AddNewStudent(context._studentContext, 'esraa')        #5


context.Courses.AddNewCourse(context._courseContext,'math')             #1
context.Courses.AddNewCourse(context._courseContext,'arabic')           #2
context.Courses.AddNewCourse(context._courseContext,'german')           #3
context.Courses.AddNewCourse(context._courseContext,'spanish')          #4
context.Courses.AddNewCourse(context._courseContext,'russin')           #5



context.StudentCourse.AddCourseToStudent(context._studentCourseContext,1,1,10)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,1,2,11)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,1,3,12)

context.StudentCourse.AddCourseToStudent(context._studentCourseContext,2,3,13)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,2,4,14)


context.StudentCourse.AddCourseToStudent(context._studentCourseContext,3,4,15)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,3,5,16)

context.StudentCourse.AddCourseToStudent(context._studentCourseContext,4,5,17)

context.StudentCourse.AddCourseToStudent(context._studentCourseContext,5,1,18)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,5,2,19)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,5,3,20)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,5,4,21)
context.StudentCourse.AddCourseToStudent(context._studentCourseContext,5,5,22)



