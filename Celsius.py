#Full Name: Kevin T Le

#Student ID: 2406054

#Chapman Email: kevle@chapman.edu

#Course Number and Section: CPSC 230-07

#In Class Programming Assignment 1: Python Basics; Exercise #2

#Purpose: This program converts and outputs Celsius temperature to Fahrenheit temperature.

print("\n\nThis program converts and outputs Celsius temperature to Fahrenheit temperature.\n")

#User enters the temperature in Celsius
temp_celsius = float(input("Enter the temperature in Celsius:\n \n"))

#Calculation of Temperature in Fahrenheit
temp_fahrenheit = (temp_celsius * (9 / 5)) + 32

print()

#Outputs Temperature in Fahrenheit
print(temp_celsius,"degrees Celsius is:",'{:.1f}'.format(temp_fahrenheit),"degrees Fahrenheit.")

print()
