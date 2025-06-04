import reports

#Generate sales reports and expenses using functions

list_tasks = []


sales_report = reports.generate_sales_report('October', 10000)
list_tasks.append(sales_report)

expenses_report = reports.generate_expenses_report('October', 5000 )

list_tasks.append(expenses_report)

print(sales_report, expenses_report)

for task in list_tasks:
    print(task)