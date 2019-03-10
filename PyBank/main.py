import os
import csv

#Define input file and output file
inputPath = os.path.join('budget_data.csv')
outputPath = os.path.join('pyBank_results.txt')

#Create function for analyzing data in input file
def financialAnalysis(financialData):

    #Initialize variables for use in subsequent for loops
    totalMonths = 0
    totalProfitLoss = 0
    listOfChanges = []
    changesPlaceholder = 0
    sumOfChanges = 0
    greatestIncrease = 0
    greatestDecrease = 0

    #Iterate through each row of input file
    for row in financialData:
        
        #Calculate total number of months (or rows) in input file
        totalMonths += 1
        
        #Calculate total profit/loss as the sum of input file's Column 2
        totalProfitLoss += int(row[1])

        #Create new table, listOfChanges: Column 1 = months; Column 2 = change in p/l from one month to next
        change = int(row[1]) - changesPlaceholder
        listOfChanges.append([row[0], change])
        changesPlaceholder = int(row[1])

    #Reset 1st row of listOfChanges; not needed for subsequent calculations
    listOfChanges[0] = ['n/a', 0]
    
    for element in listOfChanges:

        #Calculate total changes (sum of Column 2) in listOfChanges table; for use with average calc below
        sumOfChanges += element[1]

        #Identify month of greatest change and corresponding amount (positive and negative)
        if element[1] > greatestIncrease:
            greatestIncreaseMonth = element[0]
            greatestIncrease = element[1]
        elif element[1] < greatestDecrease:
            greatestDecreaseMonth = element[0]
            greatestDecrease = element[1]
    
    #Calculate average change
    averageChange = round(sumOfChanges / (len(listOfChanges) - 1), 2)

    #Print results to terminal
    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Months:  {totalMonths}')
    print(f'Total Profit/Loss:  ${totalProfitLoss}')
    print(f'Average Change:  ${averageChange}')
    print(f'Greatest Increase in Profits:  {greatestIncreaseMonth} (${greatestIncrease})')
    print(f'Greatest Decrease in Profits:  {greatestDecreaseMonth} (${greatestDecrease})')

    #Export results to text file, pyBank_results.txt
    with open(outputPath, 'w', newline = '\r\n') as txtfile:
        txtfile.write(f'Financial Analysis\r\n-----------------------------\r\nTotal Months:  {totalMonths}\r\nTotal Profit/Loss:  ${totalProfitLoss}\r\nAverage Change:  ${averageChange}\r\nGreatest Increase in Profits:  {greatestIncreaseMonth} (${greatestIncrease})\r\nGreatest Decrease in Profits:  {greatestDecreaseMonth} (${greatestDecrease})')


#Read input file and execute above financialAnalysis function
with open(inputPath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    financialAnalysis(csvreader)
    