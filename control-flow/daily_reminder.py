# daily_reminder.py
task = input("Enter your task: ")

# ... (rest of the code remains the same)

# Process task based on priority and time sensitivity
reminder_message = f"Reminder: '{task}' is a {priority} priority task. "

# Handle reminder based on priority
match priority:
  case "high":
    reminder_message += " Don't forget to complete it!"
  case "medium":
    reminder_message += " Consider completing it when you have a chance."
  case "low":
    reminder_message += " Consider completing it when you have free time."

# Check for time-bound task and add urgency message
if time_bound == "yes":
  reminder_message += "  It requires immediate attention today!"

# Print the reminder
print(reminder_message)
