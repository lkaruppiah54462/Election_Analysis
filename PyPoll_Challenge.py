#Election Analysis
#by candidate
#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
#by county
#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of counties that voted
#3. The percentage of votes by county
#4. The total number of votes by county
#5. The largest turnout county and its data (vote, %)

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

#track the winning candidate, vote count and percentage
winning_count = 0
winning_percentage = 0
winning_candidate = ""

#unique county list
counties = []

#declare the empty dictionary to cpature county and votes by county
county_votes={}

#track the county with largest turnout
largest_count = 0
largest_percentage = 0
largest_turnout_county = ""

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

        #CADIDATE
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

        #COUNTY
        #extract the county name for each row
        county_name = row[1]       
        #if the county does not match any existing county...
        if county_name not in counties:
            #Add the county name to the counties list
            counties.append(county_name)

            #begin tracking the county's vote count
            county_votes[county_name] = 0

        #add a vote to that county's count
        county_votes[county_name] += 1

#save the results to our text file
with open(file_to_save,"w") as txt_file:
    #CADIDATE
    election_results = (
        f"\nElection Results by Lakshmanan Karuppiah\n"
        f"-------------------------------------------------\n"
        f"Total Votes : {total_votes:,}\n"
        f"-------------------------------------------------\n")
    print(election_results,end="")
    #save the final vote count to text file
    txt_file.write(election_results)

    #COUNTY VOTES
    county_header = (f"County Votes:\n")
    print(county_header)
    txt_file.write(county_header)

    #Determine the percentage of votes for each county by looping through the counts
    #Iterate through the county list
    for county in counties:
        #retrieve the vote count for a county
        votes = county_votes[county]
        #calculate the % of votes
        vote_percentage = float(votes)/float(total_votes) *100
        #print each county name and % of votes
        #print(f"{county} county contributed {vote_percentage:.1f}% ({votes:,})\n")
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,} of votes)\n")
        print(county_results)
        txt_file.write(county_results)

        #Determine the largest turnout county
        #Determine if the votes is greater than the winning count
        if (votes>largest_count) and (vote_percentage > largest_percentage):
            #if true set largest_count = votes and largest_percentage = vote_percentage
            largest_count = votes
            largest_percentage = vote_percentage
            #And set the largest turnout county equal to the county's name
            largest_turnout_county = county
    largest_turnout_summary = (
        f"-------------------------------------------------\n"
        f"Largest Turnout County: {largest_turnout_county}\n"
        f"-------------------------------------------------\n")
    #save the larget turnout county's name to the text file
    txt_file.write(largest_turnout_summary)
    print(largest_turnout_summary)

    #CADIDATE VOTES
    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list
    for candidate in candidate_votes:
        #retrieve the vote count of a candidate
        votes = candidate_votes[candidate]
        #calculate the % of votes
        vote_percentage = float(votes)/float(total_votes) *100
        #print each candidate name and % of votes
        #print(f"{candidate}: received {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: received {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #Determine the winning count and candidate
        #Determine if the votes is greater than the winning count
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count : {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------------------------\n")
    #save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
    
 
