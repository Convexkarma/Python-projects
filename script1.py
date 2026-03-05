
def main():
    print ("ROT13 number encoder")
    number = int (input ("Enter your number for ROT13 encryption: "))
    rot13(number)



def rot13(n):
    
    if n<10:
        print ("Your number in ROT13:",n + 13)

    elif n<100: 
        print(int(n /10)+13,(n%10)+13 )
   
    elif n<1000:
        print (int(n/100)+13,int((n%100)/10)+13,n%10+13)

    elif n<10000:
       print(int(n/1000)+13,int((n%1000)/100)+13,int((n%100)/10)+13,(n%10)+13)
         

main()  
