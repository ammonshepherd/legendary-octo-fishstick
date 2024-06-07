wages, interest, unemployment, status, taxes_withheld = input().split()
wages = int(wages)
interest = int(interest)
unemployment = int(unemployment)
status = int(status)
taxes_withheld = int(taxes_withheld) 

agi = wages + interest + unemployment

# Check for agi first. If it's too high, don't do the rest of the calculations
if (agi > 120000):
    print("Error: Income too high to use this form")
else:
    # Set the deduction to 2400 if the status is 2 = married
    # all other status inputs are changed to 1 = single and 
    # therefore deduction is 12000
    if (status == 2):
        deduction = 24000
    else:
        status = 1
        deduction = 12000

    taxable_income = agi - deduction

    # No negative taxable income allowed
    if taxable_income < 0:
        taxable_income = 0
    
    # Calculate tax for single  
    if status == 1:
        if taxable_income <= 10000:
            tax = taxable_income * 0.10
        elif 100001 <= taxable_income <= 40000:
            tax = 1000 + ((taxable_income - 10000) * 0.12)
        elif 400001 <= taxable_income <= 85000:
            tax = 4600 + ((taxable_income - 40000) * 0.22)
        else:
            tax = 14500 + ((taxable_income - 85000) * 0.24)
    # Calculate tax for married
    else:
        if taxable_income <= 20000:
            tax = taxable_income * 0.10
        elif 200001 <= taxable_income <= 80000:
            tax = 2000 + ((taxable_income - 20000) * 0.12)
        else:
            tax = 9200 + ((taxable_income - 80000) * 0.22)

    tax = round(tax) # round the tax to get rid of cents
    
    print(f"AGI: ${agi:,}")
    print(f"Deduction: ${deduction:,}")
    print(f"Taxable income: ${taxable_income:,}")
    print(f"Federal Tax: ${tax:,}")

