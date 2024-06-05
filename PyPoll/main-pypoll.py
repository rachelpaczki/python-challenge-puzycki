# Import data for analysis
import os
import csv

candidates = []
candidate_list = {}
vote_count = 0

pypoll_csv = os.path.join("/Users/rachelpuzycki/Desktop/NW Bootcamp/python-challenge-puzycki/PyPoll/Resources/election_data.csv")
output_file = os.path.join("/Users/rachelpuzycki/Desktop/NW Bootcamp/python-challenge-puzycki/PyPoll/Analysis/PyPoll_output.txt")

# Start reader access to data in csv file
with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    Headers = next(csv_reader)

    # Loop through rows to append data
    for row in csv_reader:
        vote_count += 1
        row_cand = row[2]
        if row_cand in candidate_list.keys():
            candidate_list[row_cand] +=1
        else:
            candidate_list[row_cand] = 1

# Create Analysis output for printing
winner = ""
max_v = 0

for candidate in candidate_list.keys():
    votes = candidate_list[candidate]
    perc = 100 * (votes / vote_count)
    max_votes = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    
    #Winner
    if votes > max_v:
        winner = candidate
        max_v = votes

# Print out Analysis
print(f"Election Results\n",
      f"#----------------------------\n",
      f"Total Votes: {vote_count}\n",
      f"#----------------------------\n",
      f"Winner: {winner}\n",
      f"#----------------------------\n"
      )

# Send data to text file in analysis
with open(output_file,'w') as text:
    text.write(f"Election Results\n")
    text.write(f"#----------------------------\n")
    text.write(f"Total Votes: {vote_count}\n")
    text.write(f"#----------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"#----------------------------\n")