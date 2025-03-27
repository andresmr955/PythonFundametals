import csv
import statistics

##Read all data with sales 

monthly_sales = {}
with open('monthly_sales.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row['Month']
        sales = int(row['Sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())

## Find the average

mean_sales = statistics.mean(sales)
print(f'The average is: {mean_sales}')

median_sales = statistics.median(sales)
print(f"The median is: {median_sales}")

#Find the mode

mode_sales = statistics.mode(sales)
print(f'The mode is: {mode_sales}')

#Deviation standard
stdev_sales = statistics.stdev(sales)
print(f'The deviation standard is: {stdev_sales}')


# standard Deviation
stdev_sales = statistics.stdev(sales)
print(f'The standard deviation is: {stdev_sales}')

#Find variance
variance_Sales = statistics.variance(sales)
print(f'The variance is: {variance_Sales}')


#MAX SALES

max_sales = max(sales)
min = min(sales)

range_sales = max_sales - median_sales
print(f'Range of sales: {range_sales}')

