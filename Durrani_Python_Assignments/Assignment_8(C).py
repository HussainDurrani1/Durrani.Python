def student_database():
    students = []
    student_id = 1

    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        if name.lower() == 'stop':
            break
        
        if any(student[1] == name for student in students):
            print(f"This name '{name}' is already in the list.")
        else:

            students.append((student_id, name))
            student_id += 1

    print("\nComplete List of Students (Tuples):")
    print(students)

    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")

    if students:
        student_with_longest_name = max(students, key=lambda x: len(x[1]))
        student_with_shortest_name = min(students, key=lambda x: len(x[1]))

        print(f"The student with the longest name is: {student_with_longest_name[1]}")
        print(f"The student with the shortest name is: {student_with_shortest_name[1]}")
    else:
        print("No students were added to the database.")

student_database()
