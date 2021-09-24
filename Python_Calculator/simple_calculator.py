import math

rule = """+ Addition
- Subtraction
* Multiplication
/ Division
! Factorial
= Evaluate"""

print(rule)

sign = input("Enter the operation you want to perform: ")
myvalue = 0
value = 1

def addition():
    global myvalue
    number = int(input("How many numbers you have: "))
    for x in range(number):
        num = int(input(f"Enter the value {x+1}: "))
        myvalue = myvalue + num
    print("Sum of",str(number),"numbers is ",myvalue)
        
def subtraction():
    global myvalue
    number = int(input("How many numbers you have: "))
    mylst = [int(input(f"Enter the value {i+1}: ")) for i in range(number)]
    myvalue = mylst[0]
    for y in range(1,number):
        myvalue = myvalue - mylst[y]
    print("Difference of",str(number),"numbers is ",myvalue)

def multiplication():
    global value
    number = int(input("How many numbers you have: "))
    for x in range(1,number+1):
        num = int(input(f"Enter the value {x+1}: "))
        if num !=0:
            value = value * num
        else:
            return print('Product of',str(number),'numbers is 0')
    print("Product of",str(number),"numbers is ",value)
    
def division():
    global value
    number = int(input("How many numbers you have: "))
    try:
        for x in range(1,number+1):
            num = int(input(f"Enter the value {x+1}: "))
            value = value / num
    except:
        return print("ZeroDivision Error")
    print("Division of",str(number),"numbers is",round(value,5))

def factorial():
    num = int(input('Enter the number: '))
    try:
        fac = math.factorial(num)
        print('The factorial of',str(num),"is",fac)
    except:
        print('Invalid input')

def evaluate():
    num = input('Enter the Expression: ')
    try:
        soln = eval(str(num))
        print('Solution is',soln)
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('Invalid Expression')
    

if sign == '+':
    addition()
elif sign == '-':
    subtraction()
elif sign == '*':
    multiplication()
elif sign == '/':
    division()
elif sign == '!':
    factorial()
elif sign == '=':
    evaluate()
else:
    print('Invalid operator')
