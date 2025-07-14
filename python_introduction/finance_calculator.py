monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your monthly expenses: "))
monthlySavings = monthlyIncome - monthlyExpenses

AnnualRate = 0.05
AnnualSavings = monthlySavings * 12 + (monthlySavings * 12 * AnnualRate)
print(f"Your monthly savings are ${monthlySavings}")
print(f"Projected savings afetr one year, with interest, is ${AnnualSavings}") 