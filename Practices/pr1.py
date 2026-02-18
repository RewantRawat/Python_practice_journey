#Sum of two numbers#

first=input("Enter first number:")
second=input("Enter second number:")

sum=int(first)+int(second)
print("Sum of numbers are:",sum)

#create calculator#

first=input("Enter first number:")
operator=input("Enter Operator (+,-,*,/,%):")
second=input("Enter second number:")

first =int(first)
second=int(second)

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
else:
    print("Invalid operation")