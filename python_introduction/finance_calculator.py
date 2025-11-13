# Ask the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the user's monthly savings
monthly_savings = monthly_income - monthly_expenses

#Calculate projected savings after one year (12 months) with 5% interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display the results
print("Your monthly savings are: $", (monthly_savings))
print("Your projected savings after one year is: $", (projected_savings)) 