''' Exercises from : https://pynative.com/python-basic-exercise-for-beginners/
Given two integer numbers return their product. If the product is greater than 1000, then return their sum'''

def ex_1 (num1,num2):
    a = num1*num2
    if a >=1000 :
        return (num1+num2)
    else:
        return (a)
'''Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number'''
def ex_2(sum_range):
    prev_num = 0
    for i in range(0,sum_range):
        sum = prev_num + i
        print("The sum of previous number", prev_num," + Current number",i," is", sum)
        prev_num = i

'''Given a string, display only those characters which are present at an even index number'''
def ex_3(ipstring):
    for i in range(0,len(ipstring)):
        if i == 0:
            print (ipstring[0])
        elif i%2 == 0:
            print(ipstring[i])
        else:
            continue

'''Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string'''
def ex_4 (ipstring,n):
    if n < len(ipstring):
        print(ipstring[n:])

'''Given a list of numbers, return True if first and last number of a list is same'''
def ex_5(mylist):
    if mylist[0] == mylist[-1]:
        print("True")
    else:
        print("False")

'''Given a list of numbers, Iterate it and print only those numbers which are divisible of 5'''
def ex_6(mylist):
    for i in mylist:
        if i % 5 == 0:
            print(i)

'''Return the count of sub-string “Emma” appears in the given string'''
def ex_7 (ipstring):
    count = ipstring.count("Emma")
    print(count)

'''Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''

def ex_8(ip):
    for i in range(1, ip+1):
        for j in range(i):
            print(i,end=" ")
        print("\n")

'''Reverse a given number and return true if it is the same as the original number'''
def ex_9(ip):
    ip = str(ip)
    new_num =ip[-1]
    for i in range(-2,-(len(ip)+1),-1):
        new_num = new_num + ip[i]
    if ip == new_num:
        print("original and reverse is the same")
    else:
        print("original and reverse is not the same")
'''Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list'''
def ex_10(list1,list2):
    new_list = []
    for i in list1:
        if i%2 != 0:
            new_list.append(i)
    for i in list2:
        if i%2 == 0:
            new_list.append(i)
    print(new_list)

# list1 =  [10, 20, 23, 11, 17]
# list2 = [13, 43, 24, 36, 12]
# ex_10(list1,list2)

'''Write a code to extract each digit from an integer, in the reverse order'''
def ex_11(ip):
    i = 0
    iteration = len(str(ip))
    while i < iteration:
        output = ip % 10
        ip = ip//10
        print(output)
        i +=1

# ex_11(7536)

'''Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20'''
def ex_12(income):
    if (income <=10000):
        tax = 10000*0
        return(tax)
    else:
        income = income -10000
        if income > 10000:
            income = income - 10000
            tax = 0 + 10000*0.1 + income*0.2
        else:
            tax = 0 + income*0.1
        return (tax)
# print(ex_12(20000))

'''Print multiplication table form 1 to 10'''
def ex_13():
    for num in range(1,11):
        for i in range(1,11):
            print(num*i, end =" ")
        print("\n")
# ex_13()

'''Print downward Half-Pyramid Pattern with Star (asterisk)'''
def ex_14():
    for num in range(5,0,-1):
        for i in range(num):
            print("*", end =" ")
        print("\n")
'''Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp'''
def ex_15(base,exp):
    result =1
    for i in range(1,exp+1):
        result = result*base
    return(result)
print(ex_15(5,4))