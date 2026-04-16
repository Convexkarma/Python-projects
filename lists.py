# Tuples in python
#Their values cannot be changed btw
#Tuples use normal brackets
tup = (12,23,4,3,55,77)
print (tup[3])


#Dictionaries in python 
#Dictionaries use curly braces 

student1 = {"Name":"Emmanuel" , "Age":"17 years" , "School":"Multimedia University"}
print(student1["Name"])

'''
Both can be accessed the same way 
'''

# Yeah there's also the .get() function you can use to access the data in a dictionary 
# EG 

print (student1.get("Name"))

#output will be:
# 3
# Emmanuel
# Emmanuel


# Python lists 
# They use square brackets

Names = ['John','Jake','Edwin','Karen','Angel','Tam','Prima']
print (Names[1]) # you also use indexes to access names/values in the list