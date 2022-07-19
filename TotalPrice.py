#Full Name: Kevin T Le

#Student ID: 2406054

#Chapman Email: kevle@chapman.edu

#Course Number and Section: CPSC 230-07

#In Class Programming Assignment 1: Python Basics; Exercise #1

#Purpose: This program calculates and outputs the total price of a purchase item, given the price and the sales tax rate.

print("\n\nThis program calculates and outputs the total price of a purchase item, given the price and the sales tax rate.\n")

#User enters the Item Price and Sales Tax Rate
item_price = float(input("Enter the item purchase price: \n \n"))

sales_tax_rate = float(input("\nEnter the sales tax rate in percentage: \n \n"))

#Calculation and Output of Total Price
total_price = item_price + ((sales_tax_rate * 0.01) * item_price)

print("\nThe total price of the item is: \n \n$" '{:.2f}'.format(total_price))

print()
