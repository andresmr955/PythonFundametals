from module_balance_profitable import Active, Passive, Patrimony, MonthlyBalance




months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
matrix_balance = []

for month in months:
    balance = MonthlyBalance(month)
    balance.calculate()
    matrix_balance.append(balance.monthly_row())
#Prints results
for row in matrix_balance:
    print(f"Month: {row[0]} | Patrimony: {row[1]} | Passive: {row[2]} | Active: {row[3]} | Balanced: {row[4]}")

def calculate_balance_per_mont():
    pass

def calculate_month_profitable():
    pass