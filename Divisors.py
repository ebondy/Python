#! /usr/bin/env python3

#Author: Eric Bondy
#Divisor Practice

num = int(input("Please provide a number you'd like to get the divisors of: "))     #Prompt the user

numList = range(1, (num + 1))                                                       #Create a list from 1 to num
resultList = []                                                                     #Create an empty list

for i in numList:                                                                   #If its a divisor of the given number, add it to the list
    if num % i == 0:
        resultList.append(i)

print(resultList)                                                                   #Print the list
