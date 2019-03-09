import os
import csv

#Retrieves the document
#electioncsv = os.path.join('..''Resources', 'election_data.csv')(Regresar a este antes de enviarlo)
electioncsv="/Users/moradocuevas/Dropbox/TecBootCamp/python-challenge/PyPoll/Resources/election_data.csv"
# Method 2: Improved Reading using CSV module

m=0

votes=[]
candidate=[]
data=[]


with open(electioncsv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') #Preguntar cómo se lee esto
    print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        data.append(row)
        votes.append(row[0])
        m=m+1
        candidate.append(row[2])
print(m)


"""averages=[(x+y)/2.0 for (x,y) in zip(pl[:-1], pl[1:])]
pritn
print(averages )
#plsum=sum(pl)
pl=[int(i) for i in pl]
plsum=(sum(pl))


print("Election Results")
print("----------------------------")
print("Total Votes: "+  str (m))
print("----------------------------")
print("Total: "+ "$"+ str())
#print("Average change: " + str(plav))
print("Greatest increase in Profits: "+ str())
print()

#Net total amount of "profit/losses"

#Average change in profits
#Greatest increase in profit (date and amount)
#Decrease in losses (date and amount)"""
