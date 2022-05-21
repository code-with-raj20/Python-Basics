#Program to print the multiplication table of any number.
num1 = int(input("Enter a number: "))
num2 = 1
while num2 < 11:
    num3 = num1 * num2
    print (str(num1)+ " " + "x"+ " " + str(num2)+ " "+ "="+ " " + str(num3))
    num2 = num2 + 1
    if num2 == 11:
        break