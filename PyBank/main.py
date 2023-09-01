import os
import csv
import sys

#----------------------------------------------------------
#  PyBank Analysis
#----------------------------------------------------------

# file extensions
pybank_csv = "PyBank\\Resources\\budget_data.csv"
analysis_txt = "PyBank\\Analysis\\FinancialAnalysis.txt"
#variable to hold the total number of months analyzed
total_months = 0
#variable to hold the total profits 
total_profits = 0
#variable to hold the current value of the profits/losses
value = 0
#variable to hold the change in profits/losses
change = 0
#list to hold all the dates in the csv
dates = []
#list to hold all the profit/loss numbers in the csv
profits = []

# ----------------------------------------------------------
#  open the csv and read it, then store information about
#  the finances
# ----------------------------------------------------------
with open(pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header
    header = next(csvreader)
    # read first row of data and initialize variables with those values
    first_row = next(csvreader)
    
    total_months = total_months + 1
    total_profits = total_profits + int(first_row[1])
    value = int(first_row[1])

    # read each row and create the lists
    for row in csvreader:
        dates.append(row[0])
        # calculate change, then add to list of changes
        change = int(row[1]) - value
        profits.append(change)
        #current value of profits/losses column
        value = int(row[1])
        #increment total months
        total_months += 1
        #add profit/loss to the total
        total_profits = total_profits + int(row[1])

#calculate greatest increase from the list of profits (max)
greatest_increase = max(profits)
#find the index of greatest increase, then find date from index
greatest_increase_index = profits.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

#calculate greatest decrease from list of profits (min)
greatest_decrease = min(profits)
#find the index of greatest decrease, then find date from index
greatest_decrease_index = profits.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

#calculate average change using the lists
avg_change = sum(profits) / len(profits)

# ----------------------------------------------------------
#  Function to print the results to terminal
# ----------------------------------------------------------
def print_analysis():
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_profits)}")
    print(f"Average Change: ${str(round(avg_change,2))}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease)})")
# call print analysis
print_analysis()

# ----------------------------------------------------------
#  Print the results to txt file  
#  simplified version ref:
#  https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file
# ----------------------------------------------------------
with open(analysis_txt, "w") as text:
    sys.stdout = text
    print_analysis()
