from .art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
    }

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))
    while should_continue == True:
        operation = input("What operation do you want to perform?: ")
        for k in operations:
            if k == operation:
                symbol = k
                operation = operations[k]
        num2 = float(input("What's the second number?: "))
        output = operation(num1, num2)
        print(f"{num1} {symbol} {num2} = {output}")
        num1 = output

        answer = input("Would you like to continue calculating with this value?: ")
        if answer.lower() == "no":
            should_continue = False
            calculator()
        
calculator()