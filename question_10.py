# Program: Student Grade Management System
# This program records student names and marks,
# assigns grades, and calculates the class average.

# Function to determine grade based on mark
def get_grade(mark):
    if 80 <= mark <= 100:
        return "A"
    elif 70 <= mark <= 79:
        return "B"
    elif 60 <= mark <= 69:
        return "C"
    elif 50 <= mark <= 59:
        return "D"
    else:
        return "F"


# Main program

# Lists to store names and marks
student_names = []
student_marks = []

# Get number of students
num_students = int(input("How many students are in the class? "))

# Input student data
for i in range(1, num_students + 1):
    name = input(f"\nEnter student {i} name: ")
    mark = float(input(f"Enter mark for {name}: "))

    student_names.append(name)
    student_marks.append(mark)

# Display results
print("\nStudent Results:\n")

total_marks = 0

for i in range(num_students):
    name = student_names[i]
    mark = student_marks[i]
    grade = get_grade(mark)

    print(f"{name} - Mark: {float(mark)} - Grade: {grade}")

    total_marks += mark  # accumulate total marks

# Calculate and display class average
average = total_marks / num_students
print(f"\nClass average: {round(average, 2)}")