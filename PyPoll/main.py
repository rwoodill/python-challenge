import os
import csv

#----------------------------------------------------------
#  PyPoll Analysis
#----------------------------------------------------------


pypoll_csv = "PyPoll\\Resources\\election_data.csv"
total_rows = 0
count = 0
current_row_candidate = ""
candidate_list = []
clean_candidate_list = []

with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_rows+=1
        
        

        if current_row_candidate != row[2]:
            candidate_list.append(row[2]) 
            # print("different " + current_row_candidate)
            current_row_candidate = row[2]   
        # else:
            # print ("Same")

# ----------
# list comprehension to get rid of duplicates
# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# ---------            
    [clean_candidate_list.append(n) for n in candidate_list if n not in clean_candidate_list]

    print(clean_candidate_list)
    
