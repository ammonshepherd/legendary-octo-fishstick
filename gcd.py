num1 = int(input())
num2 = int(input())

while num1 != num2:
    if num2 > num1:
        num2 = num2 - num1
    else:
        num1 = num1 - num2
print(f"Greatest Common Denominator is: {num1}")
