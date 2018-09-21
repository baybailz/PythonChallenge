import os 
import csv 

bankData = os.path.join('budget_data.csv')
output_path = os.path.join('output.txt')

months = []
numbers = [] # (profit and losses)
difference = []

with open(bankData, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    header = next(csvreader)
   
    for row in csvreader:
        months.append(str(row[0]))
        numbers.append(int(row[1]))
        

    numMonths = 0
    numMonths = len(months)
   

    for number in numbers: 
        netTotal = sum(numbers)
    
    
    i = 0


    for i in range(len(numbers)): 
        if i > 0:
            diff = (numbers[i] - numbers[i-1])
            difference.append(diff)
        
    
    netDiff = sum(difference)
    
    averageDiff = (netDiff / len(difference))
    
    maxDiff = max(difference)
    
    minDiff = min(difference)

    max_index = difference.index(maxDiff)
    min_index = difference.index(minDiff) 

# End of calculations


print("")        
print("Finacial Analysis:")   
print("----------------------------------------------------------") 
print(f"Number of months: {int(numMonths)}")
print(f"Net Total of profit and losses: ${int(netTotal)}")
print(f"Average change: ${int(averageDiff)}")
print(f"Greatest Increase in Profits: {months[max_index+1]} ${int(maxDiff)}")
print(f"Greatest Decrease in Profits: {months[min_index+1]} ${int(minDiff)}")
print("----------------------------------------------------------") 
print("")   

# writing the new file


with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    csvwriter.writerow([''])
    csvwriter.writerow(['Financial Analysis:'])
    csvwriter.writerow(['----------------------------------------------------------'])
    csvwriter.writerow([f'Number of months: {int(numMonths)}'])
    csvwriter.writerow([f'Net Total of profit and losses: ${int(netTotal)}'])
    csvwriter.writerow([f'Average change: ${int(averageDiff)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {months[max_index+1]} ${int(maxDiff)}'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {months[min_index+1]} ${int(minDiff)}'])
    csvwriter.writerow(['----------------------------------------------------------'])    
    csvwriter.writerow([''])