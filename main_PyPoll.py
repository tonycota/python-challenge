#PyPoll
#import os and csv
import os
import csv

#variable for csv file
data = os.path.join("election_data.csv")

#establish all variables and lists

vote_number = []
vote_percentage = []
vote_total = 0
candidates = []

#read csv file

with open(data, newline = "") as csvfile:
    # have delimiter seperate columns by commas
    csv_reader = csv.reader(csvfile, delimiter = ",")
    #skip header row and store it as a variable
    header_row = next(csv_reader)
    
    #begin looping through dataset
    for row in csv_reader:
        #skip empty rows
        if len(row) == 0:
            continue
        vote_total += 1
        #if the candidate is not on the list then add them using the append method
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_number.append(1)
        else:
            index = candidates.index(row[2])
            vote_number[index] += 1
    
    for votes in vote_number:
        percent = (votes/vote_total) * 100
        #use round method to round to the third decimal point
        percent = round(percent, 3)
        vote_percentage.append(percent)

#print results
print("Election Results \n")
print("------------------------\n")
print(f"Total Votes: {str(vote_total)}\n")
print("------------------------\n")
#print out candidates and their respective vote percentile and counts
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(vote_percentage[x])}% ({str(vote_number[x])})\n")
print("------------------------\n")

#find the winner using index method
winner_index = vote_percentage.index(max(vote_percentage))
winning_candidate = candidates[winner_index]
print(f"Winner: {winning_candidate} \n")
print("----------------------- \n")

#export data to a .txt file
text_file = open("PyPoll_Analysis.txt", "w")
line1 = "Election Results\n"
line2 = "-------------------------\n"
line3 = str(f"Total Votes: {str(vote_total)}\n ")
line4 = "-------------------------\n"
text_file.write('{}\n{}\n{}\n{}\n'.format(line1 , line2 , line3 , line4))
for x in range(len(candidates)):
    line5 = str(f"{candidates[x]}: {str(vote_percentage[x])}% ({str(vote_number[x])})\n")
    text_file.write('{}\n'.format(line5))
line6 = "-------------------------\n"
line7 = str(f"Winner: {winning_candidate}\n")
line8 = "-------------------------\n"
text_file.write('{}\n{}\n{}\n'.format(line6 , line7 , line8))