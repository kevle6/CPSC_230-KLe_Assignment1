#Full Name: Kevin T Le

#Student ID: 2406054

#Chapman Email: kevle@chapman.edu

#Course Number and Section: CPSC 230-07

#In Class Programming Assignment 1: Python Basics; Exercise #4

#Purpose: This program calculates and outputs the time (24-hour clock) based on the number of seconds.

print("\n\nThis program calculates and outputs the time (24-hour clock) based on the number of seconds.\n")

#Information for The Number of Seconds in a Day
print("A single day has 86,400 seconds.\n")

#Input the Number of Seconds
input_seconds = int(input("Enter the number of seconds (Between 1 - 86400):\n\n")); print()

#Calculation of Hours, Minutes, and Seconds
total_hours = (input_seconds // (60 ** 2))

total_minutes = (input_seconds - (total_hours * 60 ** 2)) // 60

total_seconds = input_seconds - (total_hours * (60 ** 2)) - (total_minutes * 60)

#Program Prints the Time
print(input_seconds,"seconds converts to:",total_hours,"hours,",total_minutes,"minutes, and",total_seconds,"seconds.")

print()
