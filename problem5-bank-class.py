'''
Build a class called BankAccount that manages checking and savings accounts. The class has three attributes: a customer name, the customer's savings account balance, and the customer's checking account balance.

Implement the following constructor and instance methods as listed below:
    * Constructor with parameters (self, new_name, checking_balance, savings_balance) - set the customer name to parameter new_name, set the checking account balance to parameter checking_balance, and set the savings account balance to parameter savings_balance.
    * deposit_checking(self, amount) - add parameter amount to the checking account balance (only if positive)
    * deposit_savings(self, amount) - add parameter amount to the savings account balance (only if positive)
    * withdraw_checking(self, amount) - subtract parameter amount from the checking account balance (only if positive)
    * withdraw_savings(self, amount) - subtract parameter amount from the savings account balance (only if positive)
    * transfer_to_savings(self, amount) - subtract parameter amount from the checking account balance and add to the savings account balance (only if positive)
Use the following template as list of tasks:
# Task 1: Define BankAccount class
# Task 2: Define constructor with parameters to initialize instance attributes
# Task 3: Define deposit_checking()
# Task 4: Define deposit_savings()
# Task 5: Define withdraw_checking()
# Task 6: Define withdraw_savings()
# Task 7: Define transfer_to_savings()

Create a testing program in which:
* Create an account for “Joe Doe”, with a checking balance of 1000.00, and a savings balance of 2000.00
* Display the information for all accounts Joe Doe has
* Withdraw an amount of money from checking with the input value taken from the user, making sure to announce the user if the amount requested is greater than the balance
* Withdraw an amount of money from savings with the input value taken from the user, making sure to announce the user if the amount requested is greater than the balance
* Transfer an amount of money from checking to savings
* Print balance for both accounts at the end of the program.
'''
class BankAccount:
    customer_name = ''
    savings_balance = 0
    checking_balance = 0

    def __init__(self, new_name, checking_balance, savings_balance):
        self.customer_name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
    
    def deposit_checking(self, amount):
        if(amount > 0):
            self.checking_balance += amount
    
    def deposit_savings(self, amount):
        if(amount > 0):
            self.savings_balance += amount
    
    def withdraw_checking(self, amount):
        if(amount > 0):
            self.checking_balance -= amount
    
    def withdraw_savings(self, amount):
        if(amount > 0):
            self.savings_balance -= amount  
    
    def transfer_to_savings(self, amount):
        if(amount > 0):
            self.checking_balance -= amount
            self.savings_balance += amount 

if __name__ == "__main__":
    print("Creating account for Joe Doe with $1000.00 in checking and $2000.00 in savings.")
    joe_doe = BankAccount('Joe Doe', checking_balance=1000.00, savings_balance=2000.00)

    print()
    print(f'Account Information for {joe_doe.customer_name}')
    print(f'Checking Account: ${joe_doe.checking_balance:.2f}')
    print(f'Savings Account: ${joe_doe.savings_balance:.2f}')

    print()
    check_withdraw = int(input("Enter amount to withdraw from checking: $"))
    if (check_withdraw > joe_doe.checking_balance):
        print("Warning: The amount you are withdrawing is greater than your balance!")
    joe_doe.withdraw_checking(check_withdraw)

    print()
    sav_withdraw = int(input("Enter amount to withdraw from savings: $"))
    if (sav_withdraw > joe_doe.savings_balance):
        print("Warning: The amount you are withdrawing is greater than your balance!")
    joe_doe.withdraw_savings(sav_withdraw)

    print()
    print("Transfer $42 from checking to savings.")
    joe_doe.transfer_to_savings(42)
     
    print()
    print(f'Account Information for {joe_doe.customer_name}')
    print(f'Checking Account: ${joe_doe.checking_balance:.2f}')
    print(f'Savings Account: ${joe_doe.savings_balance:.2f}')
