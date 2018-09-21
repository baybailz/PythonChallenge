import os 
import csv 

# Import path and export path

pollCSV = os.path.join('election_data.csv')
outputCSV = os.path.join("election_output.txt")

# Lists

candidate = []
Khan = []
Correy = []
Li = []
OT = []

# Opening the file

with open(pollCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# skipping header

    header = next(csvreader)

# appending lists 

    for row in csvreader:
        candidate.append(str(row[2]))
    
    for row in candidate:
        if row == "Khan":
            Khan.append(str(candidate[0]) == "Khan")
    
        if row == "Correy":
            Correy.append(str(candidate[0]) == "Correy")
        
        if row == "Li":
            Li.append(str(candidate[0]) == "Li")
        
        if row == "O'Tooley":
            OT.append(str(candidate[0]) == "O'Tooley")

# Number of votes: 

numVotes = 0
numVotes = len(candidate)
khanVotes = len(Khan)
correyVotes = len(Correy)
liVotes = len(Li)
oVotes = len(OT)

 # Percentage of votes: 

khanPerc = round((khanVotes/numVotes * 100), 2)  
correyPerc = round((correyVotes/numVotes * 100), 2) 
liPerc = round((liVotes/numVotes * 100), 2)
oPerc = round((oVotes/numVotes * 100), 2)     

# Winner argument:

winner = max(khanVotes, liVotes, correyVotes, oVotes)

if winner == khanVotes:
    finalWinner = "Khan"
if winner == correyVotes:
    finalWinner = "Correy"
if winner == liVotes:
    finalWinner = "Li"
if winner == oVotes: 
    finalWinner = "O'Tooley"

# Printing in terminal:
        
print("")
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {int(numVotes)}")
print("-------------------------------")
print(f"Khan: {float(khanPerc)}% ({int(khanVotes)})")
print(f"Correy: {float(correyPerc)}% ({int(correyVotes)})")
print(f"Li: {float(liPerc)}% ({int(liVotes)})")
print(f"O'Tooley: {float(oPerc)}% ({int(oVotes)})")
print("-------------------------------")
print(f"Winner: {str(finalWinner)}")
print("-------------------------------")
print("")

# Writing new txt doc in same folder

with open(outputCSV, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    csvwriter.writerow([""])
    csvwriter.writerow(["Election Results:"])
    csvwriter.writerow(["----------------------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {int(numVotes)}"])
    csvwriter.writerow(["----------------------------------------------------------"])
    csvwriter.writerow([f"Khan: {float(khanPerc)}% ({int(khanVotes)})"])
    csvwriter.writerow([f"Correy: {float(correyPerc)}% ({int(correyVotes)})"])
    csvwriter.writerow([f"Li: {float(liPerc)}% ({int(liVotes)})"])
    csvwriter.writerow([f"O'Tooley: {float(oPerc)}% ({int(oVotes)})"])
    csvwriter.writerow(["----------------------------------------------------------"])   
    csvwriter.writerow([f"Winner: {str(finalWinner)}"])
    csvwriter.writerow([""])

    