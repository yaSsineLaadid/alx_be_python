# finance_calculator.py

# Prompt the user to enter their monthly income
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}.")

# Project Annual Savings
annual_interest = 0.05  # 5% annual interest rate

# Calculate Projected Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest)
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

