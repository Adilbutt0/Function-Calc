def add(num1,num2):

    print(num1 + num2)

def subtract(num1,num2):

    print(num1 - num2)

def multiply(num1,num2):

    print(num1 * num2)

def divide(num1,num2):

    try:
        print(num1/num2)
    except Exception as e:
        print(e)

num1 = int(input(f"give me first number".title()))

num2 = int(input(f"give me second number".title()))

opr = input(f"give me operation like (+,*,-,/)".title())

if opr == "+":

    add(num1,num2)
elif opr == "-":

    subtract(num1,num2)

elif opr == "*":

    multiply(num1,num2)

elif opr == "/":

    divide(num1,num2)
