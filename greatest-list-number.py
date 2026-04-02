numbers= [5,6,7,33,5,78,34,2,1,1,67]
max=numbers[0]
for number in numbers:
    if  max < number:
        max = number
        
print (f"Greatest number in list : {max}")