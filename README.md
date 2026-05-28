#Python Programming Worksheet 1
Topic: User Input, Lists, Loops, Conditional Statements and Functions
Instructions for Students
•	Create a folder and name it PDE1823-Python Practice worksheet
•	Write a Python program for each question.
•	Use meaningful variable names and comments where needed.
•	Test your program using the sample input provided.
•	Check whether your output matches the expected output.
•	Questions 1 to 7 are simple practice questions. Questions 8 to 10 are medium application questions.
•	After completing each question, push it on GitHub and once all questions are done, share your GiHub link with me. 
Part A: Simple Practice Questions
Question 1: Personal Greeting
Write a Python program that asks the user to enter their name and age. The program should display a greeting message.
Sample Input
Enter your name: Sarah
Enter your age: 18

Expected Output
Hello Sarah, you are 18 years old.
Welcome to Python programming!

Skills practised: user input, strings, output formatting.
Question 2: Even or Odd Number
Write a Python program that asks the user to enter a number. The program should check whether the number is even or odd.
Sample Input
Enter a number: 7

Expected Output
7 is an odd number.

Skills practised: user input, conditional statements, modulus operator.
Question 3: Simple Shopping List
Write a Python program that asks the user to enter 5 shopping items. Store the items in a list and then display the full shopping list.
Sample Input
Enter item 1: Bread
Enter item 2: Milk
Enter item 3: Eggs
Enter item 4: Rice
Enter item 5: Apples

Expected Output
Your shopping list is:
Bread
Milk
Eggs
Rice
Apples

Skills practised: lists, for loop, user input.
Question 4: Total of 5 Numbers
Write a Python program that asks the user to enter 5 numbers. Use a loop to calculate and display the total.
Sample Input
Enter number 1: 10
Enter number 2: 5
Enter number 3: 8
Enter number 4: 2
Enter number 5: 15

Expected Output
The total is: 40

Skills practised: loops, integer input, accumulator variable.
Question 5: Pass or Fail Checker
Write a Python program that asks the user to enter a mark. If the mark is 50 or above, display "Pass". Otherwise, display "Fail".
Sample Input
Enter your mark: 65

Expected Output
Result: Pass

Skills practised: conditional statements, comparison operators, user input.
Question 6: Function to Calculate Area of a Rectangle
Write a Python program with a function called calculate_area(length, width). The function should return the area of a rectangle. In the main program, ask the user to enter the length and width, call the function, and display the area.
Sample Input
Enter length: 8
Enter width: 5

Expected Output
The area of the rectangle is: 40

Skills practised: functions, parameters, return values.
Question 7: Count Positive Numbers in a List
Write a Python program that asks the user to enter 6 numbers. Store them in a list. Then count how many numbers are positive.
Sample Input
Enter number 1: 5
Enter number 2: -2
Enter number 3: 0
Enter number 4: 8
Enter number 5: -7
Enter number 6: 3

Expected Output
The numbers entered are: [5, -2, 0, 8, -7, 3]
There are 3 positive numbers.

Skills practised: lists, loops, conditional statements.
 
Part B: Medium Application Questions
These questions combine several programming concepts and are designed to take around 15 minutes each.
Question 8: Small Shop Billing System
A small shop wants a simple billing system. Write a Python program that calculates the final amount a customer has to pay.
1.    Ask the cashier how many items the customer bought.
2.    Use a loop to enter the price of each item.
3.    Store all prices in a list.
4.    Use a function called calculate_total(prices) to calculate the total bill.
5.    If the total is more than Rs 1000, apply a 10% discount.
6.    Display the original total, discount amount and final amount to pay.
Sample Input
How many items did the customer buy? 4
Enter price of item 1: 250
Enter price of item 2: 300
Enter price of item 3: 150
Enter price of item 4: 500

Expected Output
Original total: Rs 1200.0
Discount: Rs 120.0
Final amount to pay: Rs 1080.0

Skills practised: functions, loops, lists, conditional statements, arithmetic.
Question 9: Weekly Step Tracker
A fitness app wants to calculate a user's weekly activity level.
1.    Use a list called days containing Monday to Sunday.
2.    Ask the user to enter the number of steps walked for each day.
3.    Store the steps in a list.
4.    Use a function called calculate_total_steps(steps) to calculate the total.
5.    Use another function called calculate_average_steps(total) to calculate the average.
6.    Display the activity level based on the average number of steps.
Average Steps	Activity Level
8000 or more	Highly Active
5000 to 7999	Moderately Active
Below 5000	Low Activity

Sample Input
Enter steps for Monday: 7000
Enter steps for Tuesday: 8500
Enter steps for Wednesday: 6000
Enter steps for Thursday: 9000
Enter steps for Friday: 7500
Enter steps for Saturday: 10000
Enter steps for Sunday: 4000

Expected Output
Total steps this week: 52000
Average steps per day: 7428.57
Activity level: Moderately Active

Skills practised: lists, loops, functions, averages, conditional statements.
Question 10: Student Grade Management System
A teacher wants a simple program to record marks for a class.
1.    Ask the teacher how many students are in the class.
2.    For each student, ask for the student's name and mark.
3.    Store the names in one list and the marks in another list.
4.    Create a function called get_grade(mark) that returns the correct grade.
5.    Display each student's name, mark and grade.
6.    Display the class average.
Mark Range	Grade
80 to 100	A
70 to 79	B
60 to 69	C
50 to 59	D
Below 50	F

Sample Input
How many students are in the class? 3

Enter student 1 name: Andy
Enter mark for Anil: 85

Enter student 2 name: Phil
Enter mark for Priya: 72

Enter student 3 name: Kevin
Enter mark for Kevin: 45

Expected Output
Student Results:

Andy - Mark: 85 - Grade: A
Phil - Mark: 72 - Grade: B
Kevin - Mark: 45 - Grade: F

Class average: 67.33

