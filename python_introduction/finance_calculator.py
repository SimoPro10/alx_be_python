 
monthly_income = float(input("Enter your monthly income: "))
 
monthly_expenses = float(input("Enter your total monthly expenses: "))
        
monthly_savings = monthly_income - monthly_expenses
    
    
annual_savings_without_interest = monthly_savings * 12
    
annual_interest = annual_savings_without_interest * 0.05
    
projected_annual_savings = annual_savings_without_interest + annual_interest
    
    
    
print(f"Your monthly savings are ${monthly_savings:.2f}.")
    
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")