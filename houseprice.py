print ("The price of the intended house is $1 million")
credit = ""
credit = input (" What is your credit score? (1.good or 2. Bad) ")
int (credit)
for char in credit :
 if credit == 1:
    print ("You have to put down $100000 for the house ")
 elif credit == 2:
    print ("You have to put down $200000 for the house ")
 else:
    print ("Error ; no input received")     
