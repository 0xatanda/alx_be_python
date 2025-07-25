num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operators = input("Choose the operation (+, -, *, /): ")

match operators:
    case "+":
        result = int(num1 + num2)
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        result = int(num1 / num2)
        print(f"The result is {result}")
    case _ :
        print("Invalid operator selected.")