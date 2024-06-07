instructions = '''
Write a program that takes in three integers and outputs the median value (not the largest or smallest value).

Ex: If the input is:
    7
    1
    4
the output is:
    4
'''

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num2)
    else:
        print(num3)

if num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num1)
    else:
        print(num3)
        
if num3 < num1 and num3 < num2:
    if num1 < num2:
        print(num1)
    else: 
        print(num2)
        