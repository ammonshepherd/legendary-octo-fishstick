from math import ceil

wall_height = float(input("Wall height: "))
wall_width = float(input("Wall width: "))

cost_paint_can = float(input("Cost of one paint can: "))

wall_area = wall_height * wall_width

paint_coverage = 350 # one gallon of paint covers 350 square feet

paint_needed = wall_area / paint_coverage

cans_needed = ceil(paint_needed)

paint_cost = cans_needed * cost_paint_can
sales_tax = paint_cost * .07
total_cost = paint_cost + sales_tax

print(f"Wall area: {wall_area:.1f} sq ft")
print(f"Paint needed: {paint_needed:.3f} gallons")
print(f"Cans needed: {cans_needed} can(s)")
print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")