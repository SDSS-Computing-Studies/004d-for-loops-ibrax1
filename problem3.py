#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
n = input("Enter an integer smaller than ten: ")
n = int(n)
numList = (1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111)
total = (0)
for number in numList:
    for i in range(len(numList)):
        ((numList[number]))
        print(n + total)