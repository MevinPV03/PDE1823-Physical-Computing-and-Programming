# Function to calculate total steps
def calculate_total_steps(steps):
    total = sum(steps)
    return total


# Function to calculate average steps
def calculate_average_steps(total):
    average = total / 7
    return average


# Function to determine activity level
def get_activity_level(average):
    if average >= 8000:
        return "Highly Active"
    elif 5000 <= average <= 7999:
        return "Moderately Active"
    else:
        return "Low Activity"


# Main program
steps = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Input steps for each day
for day in days:
    step = int(input(f"Enter steps for {day}: "))
    steps.append(step)

# Call functions
total_steps = calculate_total_steps(steps)
average_steps = calculate_average_steps(total_steps)
activity_level = get_activity_level(average_steps)

# Display results
print("\nTotal steps this week:", total_steps)
print("Average steps per day:", round(average_steps, 2))
print("Activity level:", activity_level)