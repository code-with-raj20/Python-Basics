#Program to take 3 numbers as input ad store their first 3 positive multiples of the number in a list and display the list on the screen.
num1 = int(input("Write the 1st number: "))
num2 = int(input("Write the 2nd number: "))
num3 = int(input("Write the 3rd number: "))
m1 = num1*1,num1*2,num1*3
m2 = num2*1,num2*2,num2*3
m3 = num3*1,num3*2,num3*3
list5 = [m1,m2,m3]
print (list5)