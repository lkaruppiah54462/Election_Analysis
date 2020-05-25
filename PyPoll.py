#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
#add our dependencies
import os
import csv

#assign a variable for this file to load and the path
file_to_load = os.path.join('Resources','election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#declare the empty dictionary
candidate_votes={}

winning_count = 0
winning_percentage = 0
winning_candidate = ""

#open the election results and read the file.
with open(file_to_load) as election_data:
    #To do:read and analyze the data here.
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name for each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list
for candidate in candidate_votes:
    #retrieve the vote count of a candidate
    votes = candidate_votes[candidate]
    #calculate the % of votes
    vote_percentage = float(votes)/float(total_votes) *100
    #print the candidate name and % of votes
    print(f"{candidate}: received {vote_percentage:.1f}% ({votes:,})\n")

    #Determine the winning count and candidate
    #Determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage > winning_percentage):
        #if true set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And set the winning_candidate equal to the candidate's name
        winning_candidate = candidate
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count : {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")
print(winning_candidate_summary)



 
