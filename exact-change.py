instructions = '''Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
Ex: If the input is:
  0 
(or less than 0), the output is:
  No change 
Ex: If the input is:
  45
the output is:
  1 Quarter
  2 Dimes 
'''

# The amount of money given
amount = int(input())

dollars = 100
quarters = 25
dimes = 10
nickels = 5
pennies = 1

if amount == 0:
    print("No change")
else:
    num_dollars = amount // dollars
    after_dollars = amount % dollars
    if (num_dollars == 1):
        print("1 Dollar")
    elif num_dollars > 1:
        print(num_dollars, "Dollars")

    num_quarters = after_dollars // quarters
    after_quarters = after_dollars % quarters
    if num_quarters == 1:
        print("1 Quarter")
    elif num_quarters > 1:
        print(num_quarters, "Quarters")

    num_dimes = after_quarters // dimes
    after_dimes = after_quarters % dimes
    if num_dimes == 1:
        print("1 Dime")
    elif num_dimes > 1:
        print(num_dimes, "Dimes")

    num_nickels = after_dimes // nickels
    after_nickels = after_dimes % nickels
    if num_nickels == 1:
        print("1 Nickel")
    elif num_nickels > 1:
        print(num_nickels, "Nickels")

    num_pennies = after_nickels
    if num_pennies == 1:
        print("1 Penny")
    elif num_pennies > 1:
        print(num_pennies, "Pennies")
