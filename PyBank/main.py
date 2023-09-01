import os
import csv
import sys

#----------------------------------------------------------
#  PyBank Analysis
#----------------------------------------------------------

# file extensions
pybank_csv = "PyBank\\Resources\\budget_data.csv"
analysis_txt = "PyBank\\Analysis\\FinancialAnalysis.txt"

total_months = 0
total_profits = 0
value = 0
change = 0
dates = []
profits = []

# greatest_increase = 0
# greatest_increase_index = 0
# greatest_increase_date = "No Date Found"

# greatest_decrease = 0
# greatest_decrease_index = 0
# greatest_decrease_date = "no Date Found"

#avg_change = 0

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

    # reader each row and create the lists
    for row in csvreader:
        
        dates.append(row[0])
        # calculate change, then add to list of changes
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        total_months += 1
        total_profits = total_profits + int(row[1])

greatest_increase = max(profits)
greatest_increase_index = profits.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

greatest_decrease = min(profits)
greatest_decrease_index = profits.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

avg_change = sum(profits) / len(profits)

def print_analysis():
    #Displaying information
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_profits)}")
    print(f"Average Change: ${str(round(avg_change,2))}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease)})")
    # ----------------------------------------------------------
    #  Print the results to txt file  
    #  simplified version ref:
    #  https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file
    # ----------------------------------------------------------
    # with open(analysis_txt, "w") as text:
    #     sys.stdout = text
    #     print_results()
    #print_results()

print_analysis()
