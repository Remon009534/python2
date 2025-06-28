num1 = int(input("Enter an number:- "))
num2 = int(input("Enter an number:- "))
op = input("Choose an Operator:- ")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("WRONG OPERATORR!!")