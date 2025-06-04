'''
Tips calculation

In this challenge you will have to calculate the tip to be left by the customers of a restaurant based on their consumption.

The function calculate_tip will receive two parameters, bill_amount that represents the total cost of what has been consumed and tip_percentage that represents the percentage of tip to leave. Both values will be of float type and will always be positive, including 0. The function should return the tip value as a number.

Remember that to round to two decimal places you will have to use round(number, number of decimal places).

You will have inputs and outputs like the following 👇.

Example 1:
'''


def calculate_tip(bill_amount, tipPercentage):
   final_tips = (bill_amount * tipPercentage) / 100
   ##This help us to round the number and let 2 decimals
   return round(final_tips, 2)

print(calculate_tip(1524.33,25))