
''' https://pynative.com/python-string-exercise/#h-exercise-1a-create-a-string-made-of-the-first-middle-and-last-character
Exercise 1A: Create a string made of the first, middle and last character '''
def Ex1(input):
    x=len(input)/2
    print(input[0],input[int(x)],input[-1])
''' Exercise 1B: Create a string made of the middle three characters  '''
def Ex2(input):
    x=int(len(input)/2)
    print(input[x-1],input[x],input[x+1])
''' Exercise 2: Append new string in the middle of a given string '''
def Ex3(s1,s2):
    x=int(len(s1)/2)
    print(s1[:x]+s2+s1[x:])
''' Exercise 3: Create a new string made of the first, middle, and last characters of each input string '''
def Ex4(s1,s2):
    x = int(len(s1) / 2)
    y = int(len(s2) / 2)
    print(s1[0]+s2[0]+s1[x]+s2[y]+s1[-1]+s2[-1])
''' Exercise 4: Arrange string characters such that lowercase letters should come first '''
def Ex5(s1):
    o1 = ""
    o2 = ""
    for i in s1:
        if i.islower():
            o1 = o1+i
        else:
            o2 = o2+i
    print(o1+o2)
''' Exercise 5: Count all letters, digits, and special symbols from a given string '''
def Ex6(s1):
    digit =0
    alpha = 0
    sym =  0
    for i in s1 :
        if i.isdigit():
            digit=digit+1
        elif i.isalpha():
            alpha = alpha + 1
        else:
            sym = sym+1
    print(" Total count of characters, digits and symbols are \n Chars = ", alpha, "\n digit=", digit, "\n Symbols =", sym)

''' Exercise 6: Create a mixed String using the following rules
 Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.'''
def Ex7(s1,s2):
    output =""
    s3 = s2[::-1]
    n = min(len(s1),len(s2))
    for i in range(0,n):
        output = output+s1[i]+s2[i]
    if len(s1)>len(s2):
        output = output+s1[n:]
    else:
        output = output + s2[n:]
    print(output)
''' Exercise 7: String characters balance Test 
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.'''
def Ex8(s1,s2):
    count =0
    for i in s1:
        for j in s2:
            if i == j :
                count = count +1
                break
    if len(s1) == count:
        print("True")
    else:
        print("False")
''' Exercise 8: Find all occurrences of a substring in a given string by ignoring the case '''
def Ex9(s1,s2):
    temp_str = s1.lower()
    count = temp_str.count(s2.lower())
    print("The USA count is:", count)
''' Exercise 9: Calculate the sum and average of the digits present in a string '''
def Ex10(s1):
    count = 0
    sum = 0
    for i in s1 :
        if i.isnumeric():
            count = count +1
            sum = sum + int(i)
    print("Sum = ", sum, "Average = ", (sum/count))
''' Exercise 10: Write a program to count occurrences of all characters within a string '''
def Ex11(s1):

    for i in s1:
        count = s1.count(i)
        print(i,"=",count)
''' Exercise 11: Reverse a given string '''
def Ex12(s1):
    print(s1[::-1])
''' Exercise 12: Find the last position of a given substring '''
def Ex13(s1,s2):
    x = s1.rfind(s2)
    y = s1.rindex(s2)
    print(x,y)
''' Exercise 13: Split a string on hyphens '''
def Ex14(s1):
    print(s1.split("-"))
''' Exercise 14: Remove empty strings from a list of strings '''
def Ex15(s1):
    print(s1)
    for i in s1:
        if i:
            pass
        else:
            s1.remove(i)
    print(s1)
''' Exercise 15: Remove special symbols / punctuation from a string '''
def Ex16(s1):
    s2 =""
    for i in s1:
        if i.isalnum() or i.isspace():
            s2 = s2+i
        else:
            pass
    print(s2)
''' Exercise 16: Removal all characters from a string except integers '''
def Ex17(s1):
    s2 =""
    for i in s1:
        if i.isnumeric():
            s2=s2+str(i)
    print(s2)
''' Exercise 17: Find words with both alphabets and numbers '''
# def Ex18(s1):

''' Exercise 18: Replace each special symbol with # in the following string '''
def Ex19(s1):
    import string
    s2 =""
    for i in string.punctuation:
        s1=s1.replace(i,"#")
    print(s1)
s1 = '/*Jon is @developer & musician!!'
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Ex19(s1)