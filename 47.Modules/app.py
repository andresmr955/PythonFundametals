import reports
#Generate sales reports and expenses using functions


sales_report = reports.generate_sales_report('October', 10000)
expenses_report = reports.generate_expenses_report('October', 5000 )

print(sales_report, expenses_report)