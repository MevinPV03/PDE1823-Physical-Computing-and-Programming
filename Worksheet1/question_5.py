# Program: Pass or Fail Checker
# This program checks whether a student has passed or failed based on their mark.

# Get user input
mark = float(input("Enter your mark: "))

# Check if the mark is 50 or above
if mark >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")