#PyBank
#import csv and os
import csv
import os


#designating path to csv file with a variable
budget_data = os.path.join("budget_data.csv")

#reading csv file
with open(budget_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    #skip header row and store it as a variable
    header_row = next(reader)

    #establish all variables and lists for the dataset

    prev_revenue = 0 
    revenue_change_list = []
    month_change_list = []
    total_change = 0 
    count = 0
    total = 0

    for row in reader:
        #debugging an "index out of range" error
        # try:
        #     print(row[1])
        # except:
        #     print(row)

        #skip over empty rows
        if len(row) == 0:
            continue

        count = count + 1
        current_revenue = int(row[1])
        total = total + current_revenue

        #if statement to check changes
        if prev_revenue != 0 :
            r_change = current_revenue - prev_revenue
            revenue_change_list.append(r_change)
            month_change_list.append(row[0])
            total_change = total_change + r_change
            
        prev_revenue = current_revenue

    #find average
    avg_change = total_change / (count - 1)

    #print out all results

    print("Financial Analysis \n--------------------")
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${avg_change:.2f}')
    
    #find the biggest increase
    max_increase = max(revenue_change_list)
    max_increase_month = month_change_list[revenue_change_list.index(max_increase)]
    
    #print
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
  
    #find the biggest decrease
    max_decrease = min(revenue_change_list)
    max_decrease_month = month_change_list[revenue_change_list.index(max_decrease)]

    #print
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})") 

# exporting to a .txt file
output = open("PyBank_Analysis.txt" , "w")

line1 = "Financial Analysis\n"
line2 = "------------------\n"
line3 = str(f"Total Months: {str(count)}\n")
line4 = str(f"Total: ${str(total)}\n")
line5 = str(f"Average Change: ${str(round(avg_change,2))}\n")
line6 = str(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
line7 = str(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")
#format
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))
