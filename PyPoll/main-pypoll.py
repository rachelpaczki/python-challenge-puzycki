# Import data for analysis
import os
import csv

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")
output_file = os.path.join("..","Analysis", "PyPoll_output.txt")

# Start reader access to data in csv file

with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(pypoll_csv,delimiter=",")

# Prepare data for usage 
import pandas as pd
df = pd.read_csv(pypoll_csv)

totalballots = []
ballotData = []
candidates = []
winningvotes = 0

with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(pypoll_csv,delimiter=",")
    Headers = next(csv_reader)

    for row in csv_reader:
        ballotData.append(row[0])

# Calculate unique candidates based upon csv file
for row in ballotData:
    
    if row[2] not in candidates:
        candidates.append(row[2])

    else: 
        uniquecandidates = candidates.index(row[2])
        totalballots[uniquecandidates] += 1

# Calculate voterpercent for each unique candidate
for i in range(len(totalballots)):
    voterpercentage.append(totalballots[i]/totalvotes)

    # Convert voterpercentage to percentage
    voterpercentage = voterpercentage*100

# Calculate the overall winner from each unique candidate
for i in range(len(totalballots)):
    if totalballots > winningvotes:
        winningvotes = totalballots[i]
        winner = uniquecandidates[i]

# Create Analysis output for printing
with open(output_file,'w') as text_file:
    text_file.write(f"Election Results\n",
                  f"#-----------------------------",
                  f"Total Votes: {totalballots}\n",
                  f"#-----------------------------")

for i in range(len(candidates)):
    text_file.write(f"{uniquecandidates:[i]}: {voterpercentage[i]} ({totalballots[i]})\n")
                   
    output_file.write(f"#-----------------------------",
                      f"Winner: {winner}\n",
                      f"#-----------------------------")

# Send data to text file in analysis
with open(output_file,'r') as text_file:
    print(text_file)

