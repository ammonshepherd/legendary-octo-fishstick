wages, interest, unemployment, status, taxes_withheld = input().split()
wages = int(wages)
interest = int(interest)
unemployment = int(unemployment)
status = int(status)
taxes_withheld = int(taxes_withheld) 

agi = wages + interest + unemployment

# Set the deduction to 2400 if the status is 2 = married
# all other status inputs are changed to 1 = single and 
# therefore deduction is 12000
if (status == 2):
    deduction = 24000
else:
    status = 1
    deduction = 12000

taxable_income = agi - deduction

if taxable_income < 0:
    taxable_income = 0
    
if (agi > 120000):
    print("Error: Income too high to use this form")
else:
    print(f"AGI: ${agi:,}")
    print(f"Deduction: ${deduction:,}")
    print(f"Taxable income: ${taxable_income:,}")

