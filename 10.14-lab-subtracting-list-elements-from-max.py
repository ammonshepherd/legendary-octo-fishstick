'''
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This can be done by normalizing to values between 0 and 1, or throwing away outliers. For this program, adjust the values by subtracting each value from the maximum. Input values should be added to the list until -1 is entered.

Ex: If the input is:
    30
    50
    10
    70
    65
    -1
the output is:
    40
    20
    60
    0
    5
Your program must define and call the function:
    def get_max_int(nums)

Note: get_max_int() returns the maximum value in the list.
'''
# get a list, loop through each item.
# if the current item is larger than max
# which is initially set to zero, then 
# that is the new max. Return the max
def get_max_int(nums):
    max = 0
    for n in nums:
        if n > max:
            max = n
    return max
    
if __name__ == '__main__':
    num_list = []
    num = int(input())
    # while the input is not -1, get a number
    # and stick it in the num_list list
    while num != -1:
        num_list.append(num)
        num = int(input())
    
    # call the get_max_int function to get the max
    # and stick it in a variable
    max_num = get_max_int(num_list)
    
    # now enumerate through the list of numbers,
    # and subtract the value of each element from max number 
    for i, v in enumerate(num_list):
        num_list[i] = max_num - v
    
    # then print out the new value of each list item
    # This could have just been in the for loop above...
    for p in num_list:
        print(p)

