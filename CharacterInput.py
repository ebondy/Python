#!/usr/bin/env python3

#Simple user imput exercise

name = input("Please provide me your name: ")                                                   #prompt the user for their name
age = int(input("Please provide me the age you will be at the end of this calendar year: "))    #prompt the user for their age as an integer

print("Your name is " + name)                                                                   #print off their name
year = str((2017 - age) + 100)                                                                  #calculate the year said person will turn 100 and convert that int to a string

counter = int(input("How many times do you want to print the message?"))                        #prompt the user how many times they wish to repeat the upcoming message

print((year + " \n") * counter)                                                                 #print the message however many times on new lines
