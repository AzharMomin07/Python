first = input("enter first number:")
Operator = input("enter operator(+,-,*,/,%):")
second = input("enter second number:")

first = int(first)
second = int(second)

if Operator == "+":
    print(first + second)

elif Operator == "-":
    print(first - second)

elif Operator == "*":
    print(first * second)

elif Operator == "/":
    print(first / second)

elif Operator == "%":
    print(first % second)

else:
    print("Invalid Operator")
