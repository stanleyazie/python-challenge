# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('resources/menu_data.csv')
sales_filepath = Path('resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as menu_csv :
    menu_reader = csv.reader(menu_csv, delimiter=",")

    menu_head = next(menu_reader)

    for row in menu_reader :
        menu.append(row)


# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as sales_csv :
    sales_reader = csv.reader(sales_csv, delimiter=",")

    sales_head = next(sales_reader)

    for row in sales_reader :
        sales.append(row)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for row in sales :

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(row[-2])
    menu_item = ''


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    sales_item = row[-1]
    if sales_item not in report.keys() :
        report[sales_item] = {'01-count': 0, '02-revenue': 0, '03-cogs' : 0, '04-profit' : 0}


    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for line in menu :

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        price = float(line[-2])
        cost = int(line [-1])

        # @TODO: Calculate profit of each item in the menu data
        profit = float(line[-2]) - float(line[-1])

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sales_item == line[0] :
        
            # @TODO: Print out matching menu data
            #Create keys for and nested keys for dic
            #print(f'{line[0]} matches and is on the mennu')

            # @TODO: Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        #Else :


    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f'Total number of records is {row_count}')

# @TODO: Write out report to a text file (won't appear on the command line output)
report_path = Path("report.txt")

with open(report_path, "w") as txtfile :
    new_line = '\n'
    for item, data in report.items() :
        txtfile.write(f'{item}: \n')
        txtfile.write(f'{new_line.join("   {}: {}".format(label, result) for label, result in data.items())}\n')
        txtfile.write('\n')
        
   