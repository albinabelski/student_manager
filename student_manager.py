'''
Python dictionaries

'''
#   Task 18 — Mini project: student management system
# Build a small Student Management System using dictionaries.
students = {
    101: {
        "name": "Anna",
        "age": 24,
        "course": "Python",
        "grade": 92
    },
    102: {
        "name": "Ron",
        "age": 26,
        "course": "Python",
        "grade": 84
    }
}
# Create a menu:
while True:
    print(
        "=" * 7 + " " + "Student Management" + " " + "=" * 7,
        "",
        "1. Display students",
        "2. Add student",
        "3. Search student",
        "4. Update grade",
        "5. Delete student",
        "6. Calculate average grade",
        "7. Exit",
        sep="\n"
    )
    
    choice = input("Choose an option: ")
    
# 1. Display students (ID, name, course, grade)
    if choice == "1":
        for item, student in students.items():
            print("ID:",item,",",
                  "Name:", student["name"],",",
                  "Course:", student["course"],",",
                  "Grade:", student["grade"],";")
            print()

# 2. Add student
    elif choice == "2":
        student_id = int(input("Enter student's ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter student's course: ")
        grade = int(input("Enter grade: "))
        
        students[student_id] = {
            "name": name,
            "age": age,
            "course": course,
            "grade": grade
        }
        print()
        
# 3. Search student
    elif choice == "3":
        student_id = int(input("Enter student's ID to search: "))
            
        if student_id in students:
            student = students[student_id]
            print(
            "ID:",student_id,",",
            "Name:", student["name"],",",
            "Age:", student["age"],",",
            "Course:", student["course"],",",
            "Grade:", student["grade"],";"
            )
            print()                  
        else:
            print("Student not found")
            print()

# 4. Update grade    
    elif choice == "4":
        student_id = int(input("Enter the student's ID to update their grade: "))
        if student_id in students:
            new_grade = int(input("Enter the new grade: "))
            students[student_id]["grade"] = new_grade
            print()
        else:
            print("Student not found")
            print()

# 5. Delete student
    elif choice == "5":
        student_id = int(input("Enter the student's ID to remove: "))
        if student_id in students:
            del students[student_id]
        
        else:
            print("Student not found")
            print()
# 6. Calculate average
    elif choice == "6":
        # average = sum of all grades / number of students
        total = 0
        for student in students.values():
            total += student["grade"]
        
        average = total / len(students)
        print("The average grade: ", average)
        print()
        
# 7. Exit
    elif choice == "7":
        print("Ciao!")
        break