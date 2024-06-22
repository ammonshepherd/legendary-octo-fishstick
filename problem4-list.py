'''
Program Specifications
Write a program to calculate the minimum, maximum, mean, median, mode, and whether a list is a palindrome.
Your program should contain the following tasks:

# Step 5: Identify the mode of the list, after you sorted in ascending order.
# The mode is the value that appears most frequently. Assume that only one mode exists.
    # Hint: Use a loop to process each list element, looking for the longest sequence of identical values.
# '''
# get list of numbers from input as strings
num_list = input().split()
# convert all the numbers to integers
for n in range(len(num_list)):
    num_list[n] = int(num_list[n])

# Step 1: Find minimum and maximum values
max = 0
for i in num_list:
    if i > max:
        max = i

for n in range(len(num_list)):
    if n == 0:
        min = num_list[n]
    elif num_list[n] < min:
        min = num_list[n]


print(num_list)
print(f'min: {min}')
print(f'max: {max}')

# Step 2: Calculate mean as the sum of all values divided by the number of values
sum = 0
for i in num_list:
    sum += i

mean = sum / len(num_list)

print(f'mean: {mean:.3f}')

# Step 3: Check if palindrome, meaning values are the same from front to back and back to front. The output should be "true" or "false".

reverse_list = num_list[::-1]
print("Is palindrome?: ", end="")
if num_list == reverse_list:
    print("true")
else:
    print("false")
