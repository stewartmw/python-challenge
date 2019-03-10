import os
import csv

inputPath = os.path.join('budget_data.csv')
outputPath = os.path.join('pyBank_results.txt')

def financialAnalysis(financialData):

    totalMonths = 0
    totalProfitLoss = 0
    listOfChanges = []
    changesPlaceholder = 0
    sumOfChanges = 0
    greatestIncrease = 0
    greatestDecrease = 0

    for row in financialData:
        totalMonths += 1
        totalProfitLoss += int(row[1])
        change = int(row[1]) - changesPlaceholder
        listOfChanges.append([row[0], change])
        changesPlaceholder = int(row[1])

    listOfChanges[0] = ['n/a', 0]
    for element in listOfChanges:
        sumOfChanges += element[1]
        if element[1] > greatestIncrease:
            greatestIncreaseMonth = element[0]
            greatestIncrease = element[1]
        elif element[1] < greatestDecrease:
            greatestDecreaseMonth = element[0]
            greatestDecrease = element[1]
    
    averageChange = round(sumOfChanges / (len(listOfChanges) - 1), 2)

    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Months:  {totalMonths}')
    print(f'Total Profit/Loss:  ${totalProfitLoss}')
    print(f'Average Change:  ${averageChange}')
    print(f'Greatest Increase in Profits:  {greatestIncreaseMonth} (${greatestIncrease})')
    print(f'Greatest Decrease in Profits:  {greatestDecreaseMonth} (${greatestDecrease})')

    with open(outputPath, 'w', newline = '\r\n') as txtfile:
        txtfile.write(f'Financial Analysis\r\n-----------------------------\r\nTotal Months:  {totalMonths}\r\nTotal Profit/Loss:  ${totalProfitLoss}\r\nAverage Change:  ${averageChange}\r\nGreatest Increase in Profits:  {greatestIncreaseMonth} (${greatestIncrease})\r\nGreatest Decrease in Profits:  {greatestDecreaseMonth} (${greatestDecrease})')

with open(inputPath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    financialAnalysis(csvreader)
    