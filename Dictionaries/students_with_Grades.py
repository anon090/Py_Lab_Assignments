students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

# Print all students and their grades
print("Students:", students)

# Print specific student's grade
print("Grade of Alice:", students["Alice"])
print("Grade of Charlie:", students.get("Charlie"))

# Find all the keys from the dictionary
print("Student Names:", students.keys())

# To update a student's grade
students.update({"Charlie": "A"})
print("Updated Students:", students)

# To add a new student with a grade
students.update({"Robin": "C"})  
print("Added Robin:", students)

# To add another new student
students["Ariana"] = "B"
print("Added Ariana:", students)

# To remove the last added element from the dictionary
print("Removing item:", students.popitem())
print("After removal:", students)

# Looping over the dictionary keys
for student_name in students:
    print("Student Name:", student_name)
for student_name in students.keys():
    print("Student Name:", student_name)

# Looping over the dictionary values
for grade in students.values():
    print("Grade:", grade)

# Traversing the dictionary
for student_name, grade in students.items():
    print("Student Name:", student_name, "Grade:", grade)

# Remove a specific student and handle potential errors
removed_student = students.pop("Robin", None)  
if removed_student is not None:
    print("Removed Student Robin:", removed_student)
else:
    print("Student Robin not found.")

#print final data of students dictionary
print("Final Students:", students)
