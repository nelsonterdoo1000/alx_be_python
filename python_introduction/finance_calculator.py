# This is a python script that will manage a person's finances

# Variable Declaration



monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))


# calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses   

#calculate projected yearly savings
projected_yearly_savings = monthly_savings * 12

#calculate projected yearly interest
projected_yearly_interest = projected_yearly_savings * 0.05

#calculate total projected savings
total_projected_savings = projected_yearly_savings + projected_yearly_interest

#display results
print(f"Your monthly savings are, ${monthly_savings}")

print(f"Projected savings after one year, with interest, is: ${total_projected_savings}")























