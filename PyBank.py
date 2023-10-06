import os
import csv


#set path for the csv file
budgetDatacsv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")


#set the variables
totalMonths = 0
revenueTotal = 0
revenue = ["Profit/Losses"]
previousRevenue = 0
revenueChange = 0
greatestDecrease = ["", 9999999]
greatestIncrease = ["", 0]
averageRevenue = 0
changeList = []

#open the csv file and read it
with open('budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #loop through the rows in the file
    for row in csvreader:

        #get the total number of months by adding one to the months each time in the loop
        totalMonths += 1
        
        #get the revenue total by adding the total to each row in the sheet
        revenueTotal = revenueTotal + int(row["Profit/Losses"])

        #THIS DOES NOT WORK - but tries to get the average change in each row
        #In the notes it shows these variables outside of the loop that might be the issue
        revenueChange = int(row["Profit/Losses"]) - previousRevenue
        previousRevenue = int(row["Profit/Losses"])
        changeList = changeList + [revenueChange]

        #get the greatest increase while running the loop by checking if the last change was bigger than the current one
        if revenueChange > greatestIncrease[1]:
            greatestIncrease[1]= revenueChange
            greatestIncrease[0] = row['Date']

        #same thing but with the smallest decrease in the sheet
        elif revenueChange < greatestDecrease[1]:
            greatestDecrease[1]= revenueChange
            greatestDecrease[0] = row['Date']
    
    #gets the average revenue by adding each row that changes together and dividing them by the length of the total of rows(86)
    averageRevenue = sum(changeList)/len(changeList)      

#write the variables in a txt file 
textPath = "output.txt"
with open(textPath, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {totalMonths}\n")
    file.write(f"Total: {revenueTotal}\n")
    file.write(f"Average Change: {averageRevenue}\n")
    file.write(f"Greatest Increase in Profits: {greatestIncrease[0]} ({greatestIncrease[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} ({greatestDecrease[1]})\n")