def add_student():
    student_name = input("What is the student's name: ")
    student_id = input("What is the student's ID: ")
    return { "name" : student_name, "id" : student_id }

answer = input("Would you like to add a student: ")

if answer == 'Y':
    student = add_student()
    print(student)
else:
    print('Not creating a student then.')    print('Not creating a student then.')