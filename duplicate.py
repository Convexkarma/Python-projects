numbers = [5,4,3,2,465,56,7,8,875,4,4,3,5,769,990,6,4,3,6,46,78,909,0,67,7,87,54,545,67,545,56,3]
numbers.sort()
for number in numbers :
    if numbers.count(numbers) >=2 :
        numbers.clear()

print (numbers)        