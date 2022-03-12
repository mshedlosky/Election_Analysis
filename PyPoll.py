#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes easch candidate won
# 5. The winner of the elction based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#open the election results and read the file
with open(file_to_load) as election_data:

    #print the file object
    data = csv.reader(election_data)

    #header = next(election_data)
    #print(header)

    #print(election_data)

#to do: perform analysis.
    print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the election\n__________\nArapahoe\nDenver\nJefferson")

#Add our dependencies
import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:
    
    #to do: read and analyzedata here.
    file_reader = csv.reader(election_data)

#print each row in the csv file
    #for row in file_reader:
        #print(row)

#Read the file object with the reader function
    #read and print the header row
    headers = next(file_reader)
    print(headers)
    



