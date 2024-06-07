import math

print("Enter information for Order #1")
carpet_price = float(input("Enter carpet price per square foot: "))
room_width = int(input("Enter room width in feet: "))
room_length = int(input("Enter room length in feet: "))

print("\nEnter information for Order #2") # add new line for clarity
carpet_price2 = float(input("Enter carpet price per square foot: "))
room_width2 = int(input("Enter room width in feet: "))
room_length2 = int(input("Enter room length in feet: "))

print("\nEnter information for Order #3") # add new line for clarity
carpet_price3 = float(input("Enter carpet price per square foot: "))
room_width3 = int(input("Enter room width in feet: "))
room_length3 = int(input("Enter room length in feet: "))

# Order 1
room_area = room_width * room_length
# 20% is the carpet price times room area multiplied by .2
total_carpet_price = (carpet_price * room_area) + \
    ((carpet_price * room_area) * 0.2)

labor_cost = room_area * 0.75
sales_tax = (total_carpet_price + labor_cost) * 0.07
total_cost = total_carpet_price + labor_cost + sales_tax

print("\nOrder #1") # Print new line then heading for order 1
print(f"Room: {room_area} sq ft")
print(f"Carpet: ${total_carpet_price:.2f}")
print(f"Labor: ${labor_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Cost: ${total_cost:.2f}")

# Order 2
room_area2 = room_width2 * room_length2
# 20% is the carpet price times room area multiplied by .2
total_carpet_price2 = (carpet_price2 * room_area2) + \
    ((carpet_price2 * room_area2) * 0.2)
labor_cost2 = room_area2 * 0.75
sales_tax2 = (total_carpet_price2 + labor_cost2) * 0.07
total_cost2 = total_carpet_price2 + labor_cost2 + sales_tax2

print("\nOrder #2") # Print new line then heading for order 2
print(f"Room: {room_area2} sq ft")
print(f"Carpet: ${total_carpet_price2:.2f}")
print(f"Labor: ${labor_cost2:.2f}")
print(f"Tax: ${sales_tax2:.2f}")
print(f"Cost: ${total_cost2:.2f}")

# Order 2
room_area3 = room_width3 * room_length3
# 30% is the carpet price times room area multiplied by .3
total_carpet_price3 = (carpet_price3 * room_area3) + \
    ((carpet_price3 * room_area3) * 0.2)
labor_cost3 = room_area3 * 0.75
sales_tax3 = (total_carpet_price3 + labor_cost3) * 0.07
total_cost3 = total_carpet_price3 + labor_cost3 + sales_tax3

print("\nOrder #3") # Print new line then heading for order 3
print(f"Room: {room_area3} sq ft")
print(f"Carpet: ${total_carpet_price3:.3f}")
print(f"Labor: ${labor_cost3:.3f}")
print(f"Tax: ${sales_tax3:.3f}")
print(f"Cost: ${total_cost3:.3f}")

total_sales = total_cost + total_cost2 + total_cost3

print(f"\nTotal Sales: ${total_sales:.2f}")