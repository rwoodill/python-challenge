import os
import csv

#----------------------------------------------------------
#  PyBank Analysis
#----------------------------------------------------------

pybank_csv = "PyBank\\Resources\\budget_data.csv"
total_rows = 0
net_total_changes = 0
avg_changes = 0
greatest_increase = 0
greatest_decrease = 0


with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_rows+=1
        net_total_changes = net_total_changes + int(row[1])
       

    print(net_total_changes)
