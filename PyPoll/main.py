import os
import csv

#Retrieves the document
#electioncsv = os.path.join('..''Resources', 'election_data.csv')(Regresar a este antes de enviarlo)
electioncsv="/Users/moradocuevas/Dropbox/TecBootCamp/python-challenge/PyPoll/Resources/election_data.csv"
electiondata=
# Method 2: Improved Reading using CSV module

m=0

votes=[]
candidate=[]
data=[]
cand_op=[]
cand_vot={}
winning_candidate=""


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
        candidate_name=(row[2])
        if candidate_name not in cand_op:
            cand_op.append(candidate_name)
        cand_vot[candidate_name]=cand_vot[candidate_name]+1

#averages=[(x+y)/2.0 for (x,y) in zip(pl[:-1], pl[1:])]
#print(averages)
#plsum=sum(pl)
#pl=[int(i) for i in pl]
#plsum=(sum(pl))

with open(electiondata, newline='') as textfile:

election_res=(
f"\n Election Results \n"
f"----------------------------\n"
f"Total Votes: {m} \n"
f"----------------------------\n")
print(election_res, end="")


for candidate in cand_vot:
    votes=candidate_name.get(candidate)
    vote_per=float(votes)/float(total_votes)*100
    if(votes>winning_count):
        winning_count=votes
        winning_canditate=candidate

    voter_output= f"{candidate}:{vote_percentage:3f}% ({votes})\n"
    print ((voter_output), end="")
#txt_file.write(voter_output)

winning_candidate_summary=(

    f"----------------------------"
    f"Winner: {winning_candidate}\n"
    f"----------------------------")
print(winning_candidate_summary)

with open(electiondata, newline='') as textfile:
    electiondata.write(election_res)
    electiondata.write(voter_output)
    electiondata.write(winning_candidate_summary)
