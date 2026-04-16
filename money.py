#!/usr/local/bin/python3

networth = int(input ('''
What is your networth ?
 1. $0 - $100,000
 2. $100,001 - $500,000
 3. $500,001 - $1,000,000  
 Answer Here: '''))

if networth == 1:
    print ("\nSorry, you are not eligible for KCB platinum services\n")

elif networth == 2:
    print ("\nCongratulations , you have made the cut, enjoy KCB's platinum services\n")    

elif networth ==3 :
    print ("\nSplendid , you are more than eligible for KCB's platinum services ,looking good !!\n")

else:
    print("\nYou have entered an invalid number\n")
