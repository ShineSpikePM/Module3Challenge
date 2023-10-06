#load modules
import os 
import csv

#load file
electionDataCSV = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
#start with totalvotes = 0
totalVotes = 0
#make a list of candidate options []
candidates = []
#make a dictionary of candidate options {}
candidateVotes = {}
#create winner count
winnerCount = 0
winner = ""

#open file and start looping:
with open('election_data.csv') as csvfile:
    #set the reader, etc.w
    csvreader = csv.DictReader(csvfile)

    #read the header using next()
    headers = next(csvreader)
	
    #for each row:
    for row in csvreader:
        #add +1 total votes
        totalVotes += 1
	
        #each row contains voterId (0), county (1), candidate (2)
        #get the candidate name (index 2)
        candidate = row['Candidate']
	
        #use if candidate 'not in' candidatelist:
        if candidate not in candidates:
	        #add to the list of candidates (.append())
            candidates.append(candidate)
            #add the candidate to the dictionary as a key with a value of 1 (votes["camWilson"] = 1)
            candidateVotes[candidate] = 1
            
        #otherwise,
        #add 1 to the candidate key in dictionary (votes["camWilson"] += 1)
        candidateVotes[candidate] += 1


#loop through each candidate and see the amount of votes they had
#convert their amount of votes to a percentage of the total
outputFile = "electionResults.txt"
with open(outputFile, 'w') as txtFile:
    #create header
    header = (
        f"Election Results:\n"
        f"-----------------------\n")
    txtFile.write(header)
    txtFile.write(f"Total Votes: {totalVotes} \n")
    txtFile.write(f"-----------------------\n")
    #for loop to print the candidates and their percentage of votes
    for candidate in candidateVotes:
        
        votes = candidateVotes[candidate]
        votePercent = float(votes)/float(totalVotes)*100
        #if the amount of the current votes are greater than winner count, that person has won
        if (votes > winnerCount):
            winnerCount = votes
            winner = candidate
            
        #print the results of the election votes to a % with 3 decimals
        results = f"{candidate}: {votePercent:.3f}% ({votes})\n"
        print(results)
        txtFile.write(f"{results}\n")
    #clean up the text file and seperate the winner from the other votes
    txtFile.write(f"-----------------------\n")
    summary = (f"Winner: {winner}")
    txtFile.write(f"{summary}\n")
    txtFile.write(f"-----------------------\n")