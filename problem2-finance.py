'''
Program specifications 👍
Write a program in which you define a function that computes a future investment value at a given rate for a specified number of years. The future investment is determined using the formula:
    futureInvestmentValue = investmentAmount*(1+monthlyInterestRate)^numberOfMonths
Define a function using the following header:
    def futureInvestmentValue(investmentAmount, monthlyInterest, years):

In the test program, prompt users to enter the investment amount, and the annual interest in percent. Print a table that displays the future value for all years from 1 to 20.
Check your work using 10000 as investment amount and 5% annual interest. Make sure to calculate the monthly interest when you call the function you define.
'''
investmentAmount = float(input("Enter the investment amount (in whole dollars): $"))
annualInterestPercent = int(input("Enter the annual interest in percent: "))

# Calculate the monthly interest which is
# annual interest in decimal (annual /100) divided by 12
monthlyInterest = (annualInterestPercent / 100) / 12

# function to calculate value of investment based on starting value
# monthly interest and a number of years
def futureInvestmentValue(investmentAmount, monthlyInterest, years):
    # loop through the number of years given
    for i in range(years):
        # number of months increases every year
        numberOfMonths = (i+1) * 12
        # print out the current year
        print(f'{i+1:<6} ', end="")
        # calculate the value
        value = investmentAmount * (pow((1 + monthlyInterest),numberOfMonths))
        # print out the value
        print(f'${value:.2f}')

# Print the table header
print(f'Year  Value')
print(f'----  ----------')
# Call the function to print out the years and values
futureInvestmentValue(investmentAmount, monthlyInterest, 12)