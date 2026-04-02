phone = input("Phone: ")
number_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
}
comment = ""
for numbers in phone:
    comment += number_mapping.get(numbers ,"!") + " "
print(comment)
