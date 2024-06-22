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

# Step 4: sort the values in ascending order.
# After sorting the list, find the median, which is the value located in the middle of the list if the list has an odd number of values or the average of the middle two values, if the list has an even number of values

# Copy the list
sorted_list = num_list[:]
# Sort the new list
sorted_list.sort()
print(f'List sorted: {sorted_list}')
print('median: ', end="")

# if the length is even
if len(sorted_list) % 2 == 0:
    # get the left middle number
    left_mid = sorted_list[len(sorted_list)//2]
    # get the right middle number
    right_mid = sorted_list[(len(sorted_list)//2) + 1]
    median = (left_mid + right_mid) / 2
    # output the median
    print(f'{median:.2f}')
else:
    # otherwise print out the middle number
    print(sorted_list[len(sorted_list)//2])