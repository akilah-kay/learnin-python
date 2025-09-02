# Please write a program which asks the user for a positive integer number.
# The program then prints out a list of multiplication operations 
# until both operands reach the number given by the user. See the examples below for details:
# Please type in a number: 2
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

number = int(input("Please type in a number: "))
num1 = 1

while num1 <= number:
    num2 = 1
    while num2 <= number:
        print(f"{num1} x {num2} = {num1*num2}")
        num2 += 1
        



    
