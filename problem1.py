#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
import math
number = input("enter a number between 1-10 that will be the widht and height of a box please: ")
number = int(number)
numList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in numList:
    if num == number:
        for num in range(number):
            result = (("*") * number)
            print(result)