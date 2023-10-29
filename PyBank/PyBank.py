'''1.import libraries
2. import data and set vairables
3. iterate through data and set if-else statements to retrieve resultss
4. export findings to txt'''

#Impot Path and CSV 
from pathlib import Path
import csv

#Set file path and open CSV
csvpath = Path('Resources/budget_data.csv')

#Set vairiables 
total_months = 0
total_profit = 0
average = 0
best_month = ''
best_month_profit = 0
worst_month = ''
worst_month_profit = 0

with open(csvpath, newline='') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csvheader = next(csvreader)
    
    #iterate through the data to answer questions
    for row in csvreader :

        #Calculate the total months
        total_months += 1

        #Calculate total profit/loss
        total_profit += int(row[1])

        #Find and set best month
        if int(row[1]) > best_month_profit :
            best_month_profit = int(row[1])
            best_month = row[0]

        #Find and set worst month
        if int(row[1]) < worst_month_profit :
            worst_month_profit = int(row[1])
            worst_month = row[0]


    #Calculate Average and round to 2 decimals
    average = round(total_profit / total_months, 2)


#set path for export file
analysis = Path('analysis.txt')

#open txt file and write data to it
with open(analysis, 'w') as txtfile :
    txtfile.write('Financial Analysis')
    txtfile.write('\n----------------------------')
    txtfile.write(f'\nTotal Months: {total_months}')
    txtfile.write(f'\nTotal: ${total_profit}')
    txtfile.write(f'\nAverage Change: ${average}')
    txtfile.write(f'\nGreatest Increase in Profits: {best_month} (${best_month_profit})')
    txtfile.write(f'\nGreatest Decrease in Profits: {worst_month} (${worst_month_profit})')
