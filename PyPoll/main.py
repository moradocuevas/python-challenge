import os
import csv

#Retrieves the document
#electioncsv = os.path.join('..''Resources', 'election_data.csv')(Regresar a este antes de enviarlo)
electioncsv="/Users/moradocuevas/Dropbox/TecBootCamp/python-challenge/PyPoll/Resources/election_data.csv"
electiondata=os.path.join("Resources","election_brief.txt")
# Method 2: Improved Reading using CSV module

m=0

votes=[]
#candidate=[]
data=[]
cand_op=[]
cand_vot={}
#winning_candidate="


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
        #candidate.append(row[2])
        candidate_name=(row[2])
        if candidate_name not in cand_op:
            cand_op.append(candidate_name)
        if candidate_name not in cand_vot:
            cand_vot[candidate_name] = 0    
        cand_vot[candidate_name] = cand_vot[candidate_name]+1
        
        

#averages=[(x+y)/2.0 for (x,y) in zip(pl[:-1], pl[1:])]
#print(averages)
#plsum=sum(pl)
#pl=[int(i) for i in pl]
#plsum=(sum(pl))



election_res=(
    f"\n Election Results \n"
    f"----------------------------\n"
    f"Total Votes: {m} \n"
    f"----------------------------\n")
print(election_res, end="")


winning_count = 0

for candidate in cand_vot:
    
    votes=cand_vot[candidate]

    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate

    vote_percentage=float(votes)/float(m)*100
    vote_percentage=round(vote_percentage)

    voter_output= f"{candidate}:{vote_percentage:3f}% ({votes})\n"
    print ((voter_output), end="")
#txt_file.write(voter_output)
#print(winning_candidate)

winning_candidate_summary=(

    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"----------------------------")
print(winning_candidate_summary)

writer=open(electiondata, "w")
writer.write(election_res)
writer.write(voter_output)
writer.write(winning_candidate_summary)
