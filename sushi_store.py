#! /usr/bin/env python

# Creating a list to hold the name of the itens

shopping = ['fugu', 'ramen', 'sake', 'shiitake mushrooms', 'soy sauce',
    'wasabi']

# Creating a dictionary to hold the price of the itens

prices = {'fugu': 100.0, 'ramen': 5.0, 'sake': 45.0, 'shiitake mushrooms': 3.5,
     'soy sauce': 7.50, 'wasabi': 10.0}

# Loop 'for' to check the total
# and list the products

total = 0.00

for item in shopping:
    total += prices[item]

for table in prices:
        print(table)
        print(("." * 37 + str(prices[table])))

print (('\t\t\tTotal = ' + str(total)))
