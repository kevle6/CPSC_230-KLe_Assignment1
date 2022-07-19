#Full Name: Kevin T Le

#Student ID: 2406054

#Chapman Email: kevle@chapman.edu

#Course Number and Section: CPSC 230-07

#In Class Programming Assignment 1: Python Basics; Exercise #3

#Purpose: This program calculates and outputs the roots of a quadratic function using the quadratic formula.

#Import Math Functions
import math

print("\n\nThis program calculates and outputs the roots of a quadratic function.\n")

#Quadratic Formula
print("Quadratic Formula: a(x^2) + bx + c\n")

#First input
coef_a = int(input("Enter coefficient \"a\":\n\n")); print()

#Second input
coef_b = int(input("Enter coefficient \"b\":\n\n")); print()

#Third input
coef_c = int(input("Enter coefficient \"c\":\n\n")); print()

#Calculation of First Root
root_1 = (((-(coef_b)) + (math.sqrt(((coef_b)**2) - (4 * coef_a * coef_c))))) / (2 * (coef_a))

#Calculation of 2nd Root
root_2 = (((-(coef_b)) - (math.sqrt(((coef_b)**2) - (4 * coef_a * coef_c))))) / (2 * (coef_a))

#Program Prints the Two Roots
print("The roots of the quadratic function",coef_a,"* (x^2) +",coef_b,"* (x) +",coef_c,"is:\n\nx =", int(root_1),"& x =", int(root_2),".")

print()
