#Imports the libraries
import os
import csv
#Retrieves the document
#budgetcsv = os.path.join('..''Resources', 'budget_data.csv')(Regresar a este antes de enviarlo)
budgetcsv="/Users/moradocuevas/Dropbox/TecBootCamp/python-challenge/PyBank/Resources/budget_data.csv"
# Method 2: Improved Reading using CSV module

m=0

months=[]
pl=[]
data=[]
variables=[]
with open(budgetcsv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        data.append(row)
        pl.append(row[1])
        months.append(row[0])
        m=m+1

averages=[(x+y)/2.0 for (x,y) in zip(pl[:-1], pl[1:])]

print(averages )
#plsum=sum(pl)
pl=[int(i) for i in pl]
plsum=(sum(pl))


print("Financial Analysis")
print("----------------------------")
print("Total Months: "+  str (m))
print("Total: "+ "$"+ str())
#print("Average change: " + str(plav))
print("Greatest increase in Profits: "+ str())
print()

#Net total amount of "profit/losses"

#Average change in profits
#Greatest increase in profit (date and amount)
#Decrease in losses (date and amount)