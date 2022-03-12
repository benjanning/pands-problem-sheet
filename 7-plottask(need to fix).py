# a program that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Ben Janning

#import nump and matplotlib for the arrays and plotting the data

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#defining the line style to make the data look prettier
linestyle_str = [
     ('solid', 'solid'),      # Same as (0, ()) or '-'
     ('dotted', 'dotted'),    # Same as (0, (1, 1)) or ':'
     ('dashed', 'dashed'),    # Same as '--'
     ('dashdot', 'dashdot')]  # Same as '-.'

# create an array for the given range
xpoints = np.array(range(0, 4))

# provide mathematical equations for the squared, cubed and quartic funstions
x2 = xpoints * xpoints 
x3 = xpoints * xpoints * xpoints 
x4 = xpoints * xpoints * xpoints * xpoints

# Plotting each line.  Use different colours & styles for each
plt.plot(x2, linestyle_str = "dashed", color = "red", marker = "x", label = "x2")
plt.plot(x3, linestyle_str = "dashed", color = "blue", marker = "o", label = "x3")
plt.plot(x4, linestyle_str = "dashed", colour = "green", marker = ".", label = "x4")

# Adding a Legend
plt.legend()

#Adding a Title
plt.title("Plot of Functions")

#Adding labels to both axis
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show()

