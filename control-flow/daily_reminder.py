# daily_reminder.py
task = input("Enter your task: ")

# Get user input for priority with validation
priority = input("Priority (high/medium/low): ").lower()
valid_priorities = ["high", "medium", "low"]
while priority not in valid_priorities:
  print("Invalid priority. Please enter high, medium, or low.")
  priority = input("Priority (high/medium/low): ").lower()

# Get user input for time sensitivity with validation
time_bound = input("Is it time-bound? (yes/no): ").lower()
valid_time = ["yes", "no"]
while time_bound not in valid_time:
    print("Please answer with yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
reminder_message = f"Reminder: '{task}' is a {priority} priority task. "

# Handle reminder based on priority and time sensitivity
match priority:
  case "high":
    reminder_message += "It requires immediate attention today!"
  case "medium":
    reminder_message += "Consider completing it when you have a chance."
  case "low":
    reminder_message += "Consider completing it when you have free time."

# Print the reminder
print(reminder_message)
