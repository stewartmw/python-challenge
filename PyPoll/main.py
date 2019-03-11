import os
import csv

#Define input file and output file
inputPath = os.path.join('election_data.csv')
outputPath = os.path.join('election_results.txt')

#Create function for analyzing data in input file
def electionResults(electionData):
    
    #Initialize variables for use in subsequent for loops
    totalVotes = 0
    candidates = []
    candidateVotes = []
    winningVotes = 0

    #Iterate through each row of input file
    for row in electionData:
        
        #Calculate total number of votes (or rows) in input file
        totalVotes += 1
        
        #Create two lists: (1) distinct candidate names; (2) count of votes per candidate
        #The two lists will be in same order
        #(i.e., candidateVotes[0] will be the number of votes for candidates[0], etc.)
        if row[2] not in candidates:
            
            #Create new row with new candidate's name
            candidates.append(row[2])

            #Create new row with initial vote count of 1
            candidateVotes.append(1)
        else:

            #Add 1 to applicable vote count by referencing the index of the "candidates" table
            candidateVotes[candidates.index(row[2])] += 1

    #Calculate results; print to terminal; export to output file
    with open(outputPath, 'w', newline = '\r\n') as txtfile:
        print('Election Results')
        print('---------------------------------')
        print(f'Total Votes: {totalVotes}')
        print('---------------------------------')
        txtfile.write(f'Election Results\r\n---------------------------------\r\nTotal Votes: {totalVotes}\r\n---------------------------------\r\n')
        
        #Iterate through each record of distinct candidate names
        for person in candidates:

            #Calculate final votes per candidate; calculate percent of total vote
            finalCandidateVotes = candidateVotes[candidates.index(person)]
            candidateVotePercent = round((finalCandidateVotes * 100) / totalVotes, 3)

            #Keep track of who has the most votes as we iterate through the "candidates" table
            #Set warning flag in case of a tie
            if finalCandidateVotes > winningVotes:
                winningVotes = finalCandidateVotes
                tieWarning = False
            elif finalCandidateVotes == winningVotes:
                tieWarning = True
            
            #Print/export each candidate's individual results
            print(f'{person}: {candidateVotePercent}% ({finalCandidateVotes})')
            txtfile.write(f'{person}: {candidateVotePercent}% ({finalCandidateVotes})\r\n')
        print('---------------------------------')
        txtfile.write('---------------------------------\r\n')
        
        #Print/export winner if there is no tie; otherwise, indicate status of tie
        if tieWarning == False:
            winner = candidates[candidateVotes.index(winningVotes)]
            print(f'Winner: {winner}')
            txtfile.write(f'Winner: {winner}\r\n')
        else:
            print('There is a tie!')
            txtfile.write('There is a tie!\r\n')
        print('---------------------------------')
        txtfile.write('---------------------------------')

#Read input file and execute above financialAnalysis function
with open(inputPath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    electionResults(csvreader)