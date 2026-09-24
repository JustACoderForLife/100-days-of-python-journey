come_on = True
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
    "/": divide
}
while come_on:
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    if operation in operations:
        second_number = float(input("What's the second number?: "))
        result = operations[operation](first_number, second_number)
        print(result)
    else:
        print("Please enter a valid operation")
    confirm = input("Type 'y' to continue calculating with 5.0, or type 'n' to start a new calculation: ")
    while confirm=="y":
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        if operation in operations:
            second_number = float(input("What's the second number?: "))
            result = operations[operation](result, second_number)
            print(result)
        else:
            print("Please enter a valid operation")
        second_number = int(input("What's the second number?: "))
        result = operations[operation](result, second_number)
        print(result)
        confirm = input("Type 'y' to continue calculating with 5.0, or type 'n' to start a new calculation: ")
    else:
        come_on = False
