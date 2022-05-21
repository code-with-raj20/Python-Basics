#Program to create a python list of 6 no.s and replace their second, fourth and sixth number with the cube of the number to its immediate left.
num1 = int(input("Write the 1st number: "))
num2 = int(input("Write the 2nd number: "))
num3 = int(input("Write the 3rd number: "))
num4 = int(input("Write the 4th number: "))
num5 = int(input("Write the 5th number: "))
num6 = int(input("Write the 6th number: "))
list4 = [num1,num2,num3,num4,num5,num6]
print (list4)
list4[1] = num1*num1*num1
list4[3] = num3*num3*num3
list4[5] = num5*num5*num5
print (list4)