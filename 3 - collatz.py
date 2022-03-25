# Write a program that asks the user to input any postive integer,
# And outputs the succesive values of the calculation:
# At each step calculate the next value by taking the current value,
# And if it is even divide it by two, if it is odd, multiply by three and add one.
# Have the program end if the current value is one.
# Author: Ben Janning

#Asking the user to input a positive integer.
n = int(input("Please input a positive integer: "))

# Check if the numbers are odd or even using "Def Collatz".
def collatz(n):
    # Loop repeats until number reaches 1.
    while n > 1:
        #Print all the values listed from the number the user enters to the end.
        print(n)
        if (n % 2):
            #If result is not even, answer is multiplied by three and one added to it.
            n = 3 * n + 1

        #If number is even divide by two until you reach number one.
        else: 
             n= n//2
    print(1)

#Print the sequence of the calculation, down as far as the end number.
print ("Sequence: ")
collatz(n)

