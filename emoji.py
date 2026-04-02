message = input (">Enter your message:  ")
msg = message.split(' ')
emoji  = {
    "sadface":"😣",
              "happyface": "😁",
                           "laughface": "😂",
                                       "cryingface":"😭",
                                                    "angryface": "😡"
}
output = " "
for words in msg:
    output += emoji.get( words , "not available in the database") + " "

print (output)