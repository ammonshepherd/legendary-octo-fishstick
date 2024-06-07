wages, interest, unemployment, status, taxes_withheld = input().split()
wages = int(wages)
interest = int(interest)
unemployment = int(unemployment)
status = int(status)
taxes_withheld = int(taxes_withheld) 

agi = wages + interest + unemployment

    
if (agi > 120000):
    print("Error: Income too high to use this form")
else:
    print(f"AGI: ${agi:,}")

