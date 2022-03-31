# pands-problem-sheet
Repository for Weekly Pands Problem Sheets - Programming and Scripting

# Week 02 - Problem Sheet 1 - BMI Calculator

In the first task I was asked to calculate the BMI of a person using Python.  
I wrote the code to ask the user to input a their height and weight and converted the input to a float so 
the numbers could have decimal points.

I then defined the formula for calculating the BMI. [1]

In order to format the result to 2 decimal places I used the code “round: BMI = round(BMI, 2)
[2]

# Week 03 - Problem Sheet 2 - secondstring

In the second task I was asked to write a program that asks a user to input a string and output every second letter in reverse order.

First I asked the user to input the data as a string format. 

After trying different long winded methods, I found string slicing through w3schools.  By using string slicing I was able to set the step size (2) and direction (-1).  This enabled me to write the programme with a very short bit of code. [3]



# Week 04 - Problem Sheet 3 - Collatz

In the third task I was asked to: 
Write a program that asks the user to input any postive integer,
and outputs the succesive values of the calculation:
At each step calculate the next value by taking the current value,
And if it is even divide it by two, if it is odd, multiply by three and add one.
Have the program end if the current value is one.

I first asked the user to input a positive integer as an "int"
By using collatz I checked if the input was odd or even, by using a while loop.
The while loop tried to divide the number by 2 if it was greater than 1.
If it wasn't even, the number was multiplied by 3 and 1 added to it.
Otherwise the number was being divided by 2 until we eventually reached 1

I then printed the sequence down as far as the final number. [4] [5]






# Week 05 - Problem Sheet 4 - Weekday

In the fourth task I was asked to write a program that outputs whether or not it is a Weekday.

I first imported datetime in order to use it's functions. [6] [7] [8]

I then created a variable which was equal to the function used and assigned numbers to each day of the Week.

Using an if statement I was able to say that if the number of the day was smaller than or equal to 4 it was a Weekday. (Monday is represented by 0)

If the number was outside of this zone I could confirm it was the weekend with an else statement.





# Week 06 - Problem Sheet 5 - Square Root

In the fifth task I was asked to write a program that takes a positive floating number and outputs
an approximation of it's square root. [9]

I first asked the user for the input and converted it to a float.

I then made a function, which takes the number and got a approximate estimation of the square root by divin
it in half.

I then got a better approximation  of the Square Root by using Newton's method: 
(0.5 * (approx + (num/approx)))

By using a while loop, the approximate and better approximations were continuosly compared until the differece became close to 0.
At this point the loop stopped and gave the best approximation of the square root.  


# Week 07 - Problem Sheet 6 - Letter Frequency

In the sixth task I was asked to write a program that reads in a text file and outputs the number of e's it contains.

The first step was to make a text file, which could be read in the program and analysed.
FileName was defined as that text file.

At first I used a methid which ended up counting the ocurences of a word with the below method;
[11]

Before finding help in this method;
[12]


I made a function called letterFrequency and used a counter ("count") 
By using an if statement, for when the letter "e" occured
and increasing the count by 1 each time the programme counted the number of occurences.





# Week 08 - Problem Sheet 7 - Plot Task

For the seventh task I was asked to a write a program that displays a plot of the functions 
f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Numpy and Matplotlib were imported first, as they are necessary for this task.

I made an array called xpoints, which define the range for the given points. 

Using simple multiplication the squared, cubed and quardic functions were defined.  

Matplotlib's (plt) plot function was used to plot each line and give it a differet appearance.

I used the Matplotlib (plt) functions for a Legend, Title and labels and finally wrote plt.show() to output the result.


References:

[1] - https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g
[2] - https://www.reddit.com/r/learnprogramming/comments/n16exe/how_to_format_to_two_decimal_places_python/
[3] - https://www.w3schools.com/python/python_strings_slicing.asp
[4] - https://www.pythonpool.com/collatz-sequence-python/
[5] - https://www.tutorialspoint.com/collatz-sequence-in-python
[6] - https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
[7] - https://www.delftstack.com/howto/python/python-datetime-day-of-week/
[8] - https://www.w3schools.com/python/python_datetime.asp
[9] - https://realpython.com/python-square-root-function/
[10] - https://www.youtube.com/watch?v=99ABkygm2Xg
[11] - https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
[12] - https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/