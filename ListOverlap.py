#!/usr/bin/env python3

#Author: Eric Bondy
#List overlap practice
import random                                                                   #Import the random module

ListA = [random.randint(0, 51) for i in range(1, (random.randint(1, 51)))]      #Generate two random lists of integers between 0-50 with a random length between 1-50
ListB = [random.randint(0, 51) for i in range(1, (random.randint(1, 51)))]
ResultList = []                                                                 #Empty result list to append matching values


for i in ListA:                                                                 #Search through the two lists for matching values and avoid duplicates
    if i in ListB and i not in ResultList:
        ResultList.append(i)

print("List A is below")                                                        #Print all 3 lists to check for errors
print(ListA)
print("List B is below")
print(ListB)
print("Result List is below")
print(ResultList)
