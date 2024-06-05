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

#Set variables
totalmonths = 0
total = 0
profitlosses = []
dates = []
monthlychanges = []

# Define dates, profit_losses, and profit changes 
with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    
    for row in csv_reader:
        totalmonths += 1
        total += int(row[1])
        profitlosses.append(row[1])
        dates.append(row[0])


# Count the months avaliable in the csv file
totalmonths = len(dates)
totalmonths

# Calculate the net total for profit/losses
firstprofitloss = int(profitlosses[0])

# Set the loop
for i in range(1, len(profitlosses)):
    monthlychanges.append(int(profitlosses[i])-firstprofitloss)
    firstprofitloss = int(profitlosses[i])
    i += 1

# Calculate the average change for total profit losses
averagechange = sum(monthlychanges)/len(monthlychanges)
averagechange

# Calculate the greatest increase and decrease in profits
greatestincrease = max(monthlychanges)
greatestdecrease = min(monthlychanges)

greatestincrease, greatestdecrease

#Find month index for the Max Increase and Max Decrease
for i in range(len(monthlychanges)):
    if monthlychanges[i] == greatestincrease:
        maxindex = (i - 1)
    elif monthlychanges[i] == greatestdecrease:
        minindex = (i - 1)
    else:
        i += 1

greatest_inc = dates[maxindex]
greatest_dec = dates[minindex]

greatest_inc, greatest_dec

# Create Analysis output for printing
analysisoutput = (f"Financial Analysis\n",
                  f"#-----------------------------",
                  f"Total Months: {totalmonths}\n",
                  f"Total: ${total}\n",
                  f"Average Change: ${averagechange}\n",
                  f"Greatest Increase in Profits: {greatest_inc} (${greatestincrease})\n",
                  f"Greatest Decrease in Profits: {greatest_dec} (${greatestdecrease})\n"
)

# Print out analysis output
print(analysisoutput)

# Send data to text file in analysis
with open(output_file,'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"#-----------------------------\n")
    text.write(f"Total Months: {totalmonths}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${averagechange}\n")
    text.write(f"Greatest Increase in Profits: {greatest_inc} (${greatestincrease})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_dec} (${greatestdecrease})\n")

    