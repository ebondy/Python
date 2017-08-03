#!/usr/bin/env python3

#Author: Eric Bondy
#Simple conditional statement practice as well as modulo arithmetic

number = int(input("Please input a number you wish to evaluate: "))     #Prompt the user to imput a number to evaluate

if number % 4 == 0:                                                     #Check if its a multiple of 4
    print("The number you input is a multiple of 4")
elif number % 2 == 0:                                                   #If not a multiple of 4, check if its even
    print("The number you input is even")
else:                                                                   #Otherwise print that its odd
    print("The number you input is odd")

num = int(input("Please input a number to check: "))                    #Prompt the user for a number to check
check = int(input("Please input a number to divide by: "))              #Prompt the user for a number to divide by

if num % check == 0:                                                    #Check if they divide evenly
    print("The number you selected divides evenly")
else:                                                                   #If not print that they do not
    print("The number you selected does not divide evenly")
