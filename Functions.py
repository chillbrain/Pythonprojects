'''Exercise 1: Create a function that can accept two arguments name and age and print its value'''
def Ex_1(name,age):
    print("name is ",name,"age is ", age)

'''Exercise 2: Write a function func1() such that it can accept a variable length of  argument and print all arguments value'''
def Ex_2(*args):
    for i in args:
        print(i)

'''Exercise 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. 
And also it must return both addition and subtraction in a single return call'''
def Ex_3(var1, var2):
    sum = var1 + var2
    sub = var1 - var2
    return(sum,sub)

#print(Ex_3(40,10))

'''Exercise 4: Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. 
If the salary is missing in the function call assign default value 9000 to salary'''
def Ex_4(emp_name, emp_sal =9000):
    print("Employee Name is ", emp_name)
    print("Employee Salary is ", emp_sal)

'''Exercise 5: Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it'''
def Ex_5(a, b):
    def add_num(a,b):
        return(a+b)
    res = add_num(a,b)
    return(res+5)

'''Exercise 6: Write a recursive function to calculate the sum of numbers from 0 to 10'''
def Ex_6(num):
    if num:
        return num + Ex_6(num-1)
    else:
        return 0
#print(Ex_6(10))

'''Exercise 7: Assign a different name to function and call it through the new name
Below is the function displayStudent(name, age). Assign a new name showStudent(name, age) to it and call through the new name
'''
def Ex_7(name,age):
    print(name,age)

ShowStudent = Ex_7
#ShowStudent("Emma",26)

'''Exercise 8: Generate a Python list of all the even numbers between 4 to 30'''
def Ex_7(l_limit,u_limit):
    res_list = []
    for i in range(l_limit, u_limit+1):
        if i % 2 == 0:
            res_list.append(i)
    return(res_list)

#print(Ex_7(4,30))

'''Exercise 9: Return the largest item from the given list
aList = [4, 6, 8, 24, 12, 2]'''
def Ex_8(alist):
    print(max(alist))

def Ex_8_1(alist):
    j = alist[0]
    for i in alist:
        if j < i:
            j = i
    return(j)
alist = [4, 6, 8, 24, 12, 2]
print(Ex_8_1(alist))