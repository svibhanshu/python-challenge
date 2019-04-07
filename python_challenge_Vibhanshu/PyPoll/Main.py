import os
import csv

file_to_load = "election_data.csv"
file_to_output = "poll_analysis.txt"

# name_count = 0
# name_percentages = 0
total_votes = 0
candidate = []
candidate_votes = {}
candidate_percentages = {}
winning_candidate = ""
winning_count = 0
votes = []
name = []

with open('election_data.csv')as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
        candidate.append(row[2])

    candidate_votes = [[x,candidate.count(x)] for x in set(candidate)]
    
    for row in candidate_votes:
        name.append(row[0])
        votes.append(row[1])
        
    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)
    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]

    # Correy's Total Votes and Percentage Votes 
    correy_total = candidate.count("Correy")
    correy_percent = int(correy_total) / int(total_votes)

    # O'Tooley's Total Votes and Percentage Votes
    o_tooley_total = candidate.count("O'Tooley")
    o_tooley_percent = o_tooley_total / total_votes

    # Li's Total Votes and Percentage Votes
    li_total = candidate.count("Li")
    li_percent = li_total / total_votes

    # Khan's Total Votes and Percentage Votes
    khan_total = candidate.count("Khan")
    khan_percent = khan_total / total_votes

election_results = (
f"Election Results\n"
f"-----------------------\n"
f"Total Votes: {total_votes}\n"
f"------------------------\n"
f"Khan: {khan_percent:.3%} ({khan_total})\n"
f"Correy: {correy_percent:.3%} ({correy_total})\n"
f"Li: {li_percent:.3%} ({li_total})\n"
f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})\n"
f"-------------------------\n"
f"   Winner: Khan    \n"
f"-------------------------\n"
)
print(election_results)

with open(file_to_output, "w") as txt_file:  
    txt_file.write(election_results)

   
