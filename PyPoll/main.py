import os
import csv

# ----------------------------------------------------------
#  PyPoll Analysis
# ----------------------------------------------------------

#file extension
pypoll_csv = "PyPoll\\Resources\\election_data.csv"
#variable to hold total votes
total_votes = 0
#list to hold candidate names
# candidate_list = []
#list to hold number of votes per candidate
# num_votes = []
#dictionary to hold name : number of votes
candidate_votes = {}
#dictionary used to calculate percentage votes per candidate
percentage_votes = {}
winner = 0
winner_name = ""
# ----------------------------------------------------------
#  open the csv and read it, then store information about
#  the candidates
# ----------------------------------------------------------
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    header = next(csvreader)

    #for each row in the file... 
    for row in csvreader:
        #...add one to the total votes
        total_votes += 1
        #... if the candidate is in the dictionary
        if row[2] in candidate_votes:
            #...add the name and one to the votes received by candidate
            candidate_votes[row[2]] += 1
        else:
            #...if not in candidate_votes already, add the name and start the vote count at 1
            candidate_votes[row[2]] = 1
    
    # iterate through the candidate_votes dictionary
    for k, v in candidate_votes.items():
        #...find the percentage votes for each candidate
        percentage_votes[k] = round((v / total_votes)* 100, 3)
        #... find the greatest value (num of votes) in the dictionary
        if v > winner:
            winner = candidate_votes[k]
            winner_name = k

#----------------------------------------------------------
#  Function to print the results
#----------------------------------------------------------
def print_results():
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for key, val in candidate_votes.items():
        print(f"{key}: {str(percentage_votes[key])}% ({candidate_votes[key]})")
    print("-------------------------")
    print(f"Winner: {winner_name}")
    print("-------------------------")

# call print_results
print_results()
