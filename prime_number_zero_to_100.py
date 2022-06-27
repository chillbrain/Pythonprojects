def divide (val1,val2):
    quotient = val1/val2
    reminder = val1%val2
    return (reminder,quotient)

def isprime():
    for number in range(1,101):
        count = 0
        for i in range(2,number//2+1):
            reminder,quotient = divide(number,i)
            if reminder == 0:
                count += 1
                break
        if count == 0 and number !=1 :
            prime_number.append(number)




prime_number = []
isprime()
print(prime_number)



