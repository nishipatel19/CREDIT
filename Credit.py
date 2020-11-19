#asks user for CC number
cc = input (str ("What is the credit card number you wish to test?"))

sum_1 = 0 
sum_2 = 0 
final = 0 
lengthcc = len(cc)

for n in range (len(cc)-2, -1, -2):
    digit = int (cc[n]) *2
    if digit <10:
        sum_1 +=digit 
    else:
        digit = (digit//10 + digit%10)
        sum_1 += digit

for m in range (len(cc)-1, -1, -2):
    digit = int (cc[m])
    sum_2 += digit

final = sum_1 + sum_2 
print (final)

if final%10 ==0:
    if lengthcc ==15 and int(cc[0]) == 3 and (int (cc[1])==7 or int (cc[1])==4):
        print ("AMEX.")
    elif (lengthcc ==13 or lengthcc ==16) and (int (cc[0])==4):
        print ("VISA.")
    elif lengthcc ==16 and int (cc[0])==5 and (int (cc[1])==1 or int (cc[1])==2 or int (cc[1])==3 or int (cc[1])==4 or int (cc[1])==5):
        print ("MASTERCARD.")
    else:
        print ("INVALID.")

