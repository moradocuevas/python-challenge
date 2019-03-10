#Imports the libraries
import os
import csv
#import fstring
#Retrieves the document
#budgetcsv = os.path.join('..''Resources', 'budget_data.csv')(Regresar a este antes de enviarlo)
budgetcsv="/Users/moradocuevas/Dropbox/TecBootCamp/python-challenge/PyBank/Resources/budget_data.csv"
outputfile=os.path.join("Analysis", "budget_analysis.txt")
# Method 2: Improved Reading using CSV module
month_of_change=[]
m=0
net_change_list=[]
months=[]
pl=[]
data=[]
variables=[]
gi=["",0]
gd=["",99999999999999999999999999]
average_values=[]

with open(budgetcsv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        data.append(row)
        pl.append(int(row[1]))
        months.append(row[0])
        m=m+1
        prev_net=int(row[1])
        net_change=int(row[1])-prev_net
        net_change_list=net_change_list+ [net_change]
        month_of_change=month_of_change+[row[0]]
        net_monthly_average=sum(net_change_list)/len(net_change_list)
        average_values.append(net_monthly_average)
#¿Cuál es el proceso de pensamiento para generar un for que dé los promedios?


#Gives out the biggest increase and the smallest decrease.

plmax=max(net_change_list)
plmin=min(net_change_list)
suma=sum(pl)
#Structures the info

output=(
f"\n Financial Analysis\n"
#f"----------------------------\n"
#f"Total Months: + {m} \n"
#f"Total: $ {} \n" 
#f"Greatest increase in Profits: {plmax} \n" #LOS METODOS DE GREATEST N SHIT ME ESTAN FALLANDO
#f"Greatest Decrease in Profits: {plmin} \n"
)

#print(output)
outputfile.write(output) #outputfile es una str, hay que abrir el archivo para poder usar write()


