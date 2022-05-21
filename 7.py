#Program to print factorialorial of any number.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of",num,"is",factorial)
