#!/usr/bin/env python3

#Author: Eric Bondy
#Simple List manipulation practice

ListL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                                                             #Declare the 3 lists needed
NewListL = []
UserListL = []

for i in ListL:                                                                                     #For loop that cycles through the elements in the list and prints out those less than 5
    if i < 5:
        print(i)

for i in ListL:                                                                                     #For loop that cycles through the elements in the list and adds them to a new list if they're less than 5
    if i < 5:
        NewListL.append(i)

print(NewListL)

num = int(input("Please input a number you wish you derive all less than of from the list: "))      #Prompt user for a number

for i in ListL:                                                                                     #One last for loop that cycles through the list and creates a new list containing elements less than the user derived number
    if i < num:
        UserListL.append(i)

print(UserListL)
