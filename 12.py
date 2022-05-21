#Program to create a python list of 6 no.s and replace their 3rd and 4th item in the list with the product of the last two items of the list and print the list.
num1 = int(input("Write the 1st number: "))
num2 = int(input("Write the 2nd number: "))
num3 = int(input("Write the 3rd number: "))
num4 = int(input("Write the 4th number: "))
num5 = int(input("Write the 5th number: "))
num6 = int(input("Write the 6th number: "))
list3 = [num1,num2,num3,num4,num5,num6]
product = num5*num6
list3[2] = product
list3[3] = product
print(list3)