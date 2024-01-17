# Import data for analysis
import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")
output_file = os.path.join("..","Analysis", "PyBank_output.txt")

# Start reader access to data in csv file

with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(pybank_csv,delimiter=",")

# Prepare data for usage 
import pandas as pd
df = pd.read_csv(pybank_csv)

date = []
profit_losses = []
profitchanges = []

# Define dates, profit_losses, and profit changes 
with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(pybank_csv,delimiter=",")
    Headers = next(csv_reader)

    for row in csv_reader:
        date.append([0])
        profit_losses.append([1])


# Count the months avaliable in the csv file
totalmonths = len(date)

# Calculate the net total for profit/losses
totalprofitlosses = 0

for i in totalprofitlosses:
    totalprofitlosses = i +totalprofitlosses

changeprofitlosses = [totalprofitlosses[i+1]+totalprofitlosses[i] for i in range(totalmonths)]

# Calculate the average change for total profit losses
averagechange = average(changeprofitlosses)

# Calculate the greatest increase and decrease in profits
greatestincrease = 0
greatestdecrease = 0

for i in range(len(date)-1):
    if totalprofitlosses[i] > greatestincrease:
        greatestincrease = totalprofitlosses[i]

    if totalprofitlosses[i] < greatestdecrease:
        greatestdecrease = totalprofitlosses[i]

# Create Analysis output for printing
analysisoutput = (f"Financial Analysis\n",
                  f"#-----------------------------",
                  f"Total Months: {totalmonths}\n",
                  f"Total: ${totalprofitlosses}\n",
                  f"Average Change: ${averagechange}\n",
                  f"Greatest Increase in Profits: ${greatestincrease}\n",
                  f"Greatest Decrease in Profits: ${greatestdecrease}\n"
)

# Print out analysis output
print(analysisoutput)

# Send data to text file in analysis
with open(output_file,'w') as textfile:
    textfile.write(analysisoutput)
    