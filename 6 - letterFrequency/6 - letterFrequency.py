# A program that reads in a text file and outputs the number of e's it contains.
# Author: Ben Janning

# Define the file that will be read
fileName = "e.txt"

# Defining a function called "letterFrequency", which will count the amount of e's.
def letterFrequency(fileName):
    # Open the text document in read-text mode as 'f':
    with open(fileName, "rt") as f:
        # make a variable, which is equal to the document within the programme.
        text = f.read()
        # setting up a counter, which begins on 0.
        count = 0
        # Using a for loop, increase the count by 1 for each instance of "e", or "E".
        for letter in text:
            if letter == 'e':
                count += 1
            elif letter == 'E':
                count += 1
        return count

# Take the ouput of the program and give it a name (variable):
number = letterFrequency(fileName)

# Printing a message and converting the result to a string (as it can't be read as an integer)" 
print("The number of occurences of the letter 'e': " + str(number))