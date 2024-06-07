from math import ceil

wall_height = float(input("Wall height: "))
wall_width = float(input("Wall width: "))

cost_paint_can = float(input("Cost of one paint can: "))

wall_area = wall_height * wall_width

paint_coverage = 350 # one gallon of paint covers 350 square feet

paint_needed = wall_area / paint_coverage

print(f"Wall area: {wall_area:.1f} sq ft")
print(f"Paint needed: {paint_needed:.3f} gallons")