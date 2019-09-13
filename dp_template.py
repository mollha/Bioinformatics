#!/usr/bin/python
import time
import sys
import numpy

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

def populateMatrices(i,j):                  
    for x in range(0,j+1):                  #Iterates between 0 and number of columns
        Scoring[0,x] = -2*x                 #Assigns x multiples of -2 to top row cells
        Backtracking[0,x] = ' L '           #Assigns L to top row cells
    for x in range(0, i+1):                 #Iterates between 0 and number of rows
        Scoring[x,0] = -2*x                 #Assigns x multiples of -2 to left-most column cells in scoring matrix
        Backtracking[x,0] = ' U '           #Assigns L to left-most column cells in backtracking matrix
    Backtracking[0,0] = 'END'               #Assigns END to cell[0,0] of backtracking matrix
    
    for y in range(1, j+1):                         #Iterates across all columns except column 0 (already scored)
        for x in range(1, i+1):                     #Iterates across all rows except row 1 (already scored)
            D = score(x,y)+ Scoring[x-1, y-1]       #Assigns the score of the cell to the upper diagonal left added to the score of cell(x,y) to variable D
            U = Scoring[x-1,y]-2                    #Assigns the score of the cell above -2 to variable U
            L = Scoring[x,y-1]-2                    #Assigns the score of the cell to the left -2 to variable L
            maxScore = max(D,U,L)                   #Assigns the largest of the variables D, U and L to variable maxScore
            Scoring[x,y] = maxScore                 #Assigns maxScore to cell[x,y] of the scoring matrix
            if D == maxScore:                       #If the max score comes from score(x,y)+ Scoring[x-1, y-1]
                Backtracking[x,y] = ' D '           #Assign letter D to cell [x,y] of backtracking matrix
            elif L == maxScore:                     #If the max score comes from Scoring[x-1,y]-2
                Backtracking[x,y] = ' L '           #Assign letter L to cell [x,y] of backtracking matrix
            else:                                   #If the max score comes from Scoring[x-1,y]-2
                Backtracking[x,y] = ' U '           #Assign letter U to cell [x,y] of backtracking matrix
    
def score(i,j):                             #scoring system
    s1 = seq1[j-1]                          #Assigns character in position [j-1] of seq1 to variable s1                                  
    s2 = seq2[i-1]                          #Assigns character in position [i-1] of seq2 to variable s2
    if s1==s2:                              #If these characters match
        if s1 =='A' or s1 == 'C':           #and if they are As or Cs
            return 3                        #return a score of 3
        elif s1 =='G' or s1 == 'T':         #or if they are Gs or Ts
            return 2                        #return a score of 2
    else:                                   #otherwise
        return -1                           #return a score of -1 which indicates a mismatch
# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

    

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer

file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

i = len(seq2); j = len(seq1)                                    #Assigns the length of sequences 2 and 1 to variables i and j respectively
Scoring = numpy.zeros((i+1, j+1), dtype = int)                  #Initialises the scoring matrix
Backtracking = numpy.empty((i+1, j+1), dtype = object)          #Initialises the backtracking matrix
populateMatrices(i,j)                                           #Calls the function which populates both the scoring and backtracking matrix
best_score = Scoring[i,j]                                       #Assigns the score of the best scoring alignment to variable best_score
seq1A = ''; seq2A = '';                                         #Initialises variables seq1A and seq2A as empty strings

while j>0 or i>0:                                   #Whilst at least one of i or j is still greater than 0
    string = Backtracking[i,j]                      #Assign the string contained in cell[i,j] of backtracking matrix to variable string
    letter = string[1]                              #Assign the 2nd character of the string to a different variable, letter (the character containing either L,D or U)
    if letter == 'L':                               #if variable letter is L
        seq1A += seq1[j-1]                          #Take the j-1th letter from sequence 1 and add it to string seq1A
        seq2A += '-'                                #Add a gap to string seq2A
        j -= 1                                      #Subtract 1 from variable j
    elif letter == 'U':                             #if variable letter is U
        seq1A += '-'                                #Add a gap to string seq1A
        seq2A += seq2[i-1]                          #Take the i-1th letter from sequence 2 and add it to string seq2A
        i -= 1                                      #Subtract 1 from variable i
    elif letter == 'D':                             #if variable letter is D
        seq1A += seq1[j-1]                          #Take the j-1th letter from sequence 1 and add it to string seq1A
        seq2A += seq2[i-1]                          #Take the i-1th letter from sequence 2 and add it to string seq2A
        j -= 1                                      #Subtract 1 from variable j
        i -= 1                                      #Subtract 1 from variable i
best_alignment = [seq1A[::-1], seq2A[::-1]]         #Uses string splicing to reverse strings seq1A and seq2A (as they are currently backwards) and assign the array to best_alignment

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

