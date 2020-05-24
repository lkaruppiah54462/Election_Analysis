#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
import os
import csv
#assign a variable for this file to load and the path
file_to_load = os.path.join('Resources','election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:
    #To do:read and analyze the data here.
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    print(headers)
# Using the open() function with the "w" mode we will write data to the file.



# Close the file
#outfile.close()
