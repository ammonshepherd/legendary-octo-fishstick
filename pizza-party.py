# Week 4. Problem 2: Pizza Party

import math

people = int(input("Number of people: "))
slices_per_person = float(input("Number of slices/person: "))
one_pizza_cost = float(input("Cost of one pizza: "))

print()
people2 = int(input("Number of people: "))
slices_per_person2 = float(input("Number of slices/person: "))
one_pizza_cost2 = float(input("Cost of one pizza: "))

print()
people3 = int(input("Number of people: "))
slices_per_person3 = float(input("Number of slices/person: "))
one_pizza_cost3 = float(input("Cost of one pizza: "))

slices_per_pizza = 8
slices_needed = people * slices_per_person
pizzas_needed = math.ceil(slices_needed / slices_per_pizza)
pizza_cost = one_pizza_cost * pizzas_needed
sales_tax = pizza_cost * 0.07
delivery_charge = (pizza_cost + sales_tax) * 0.2
total = pizza_cost + sales_tax + delivery_charge

slices_per_pizza2 = 8
slices_needed2 = people2 * slices_per_person2
pizzas_needed2 = math.ceil(slices_needed2 / slices_per_pizza2)
pizza_cost2 = one_pizza_cost2 * pizzas_needed2
sales_tax2 = pizza_cost2 * 0.07
delivery_charge2 = (pizza_cost2 + sales_tax2) * 0.2
total2 = pizza_cost2 + sales_tax2 + delivery_charge2

slices_per_pizza3 = 8
slices_needed3 = people3 * slices_per_person3
pizzas_needed3 = math.ceil(slices_needed3 / slices_per_pizza3)
pizza_cost3 = one_pizza_cost3 * pizzas_needed3
sales_tax3 = pizza_cost3 * 0.07
delivery_charge3 = (pizza_cost3 + sales_tax3) * 0.2
total3 = pizza_cost3 + sales_tax3 + delivery_charge3

weekend_total = total + total2 + total3

print()
print("Friday Night Party")
print(f"{pizzas_needed} Pizzas: ${pizza_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Delivery: ${delivery_charge:.2f}")
print(f"Total: ${total:.2f}")

print()
print("Saturday Night Party")
print(f"{pizzas_needed2} Pizzas: ${pizza_cost2:.2f}")
print(f"Tax: ${sales_tax2:.2f}")
print(f"Delivery: ${delivery_charge2:.2f}")
print(f"Total: ${total2:.2f}")

print()
print("Sunday Night Party")
print(f"{pizzas_needed3} Pizzas: ${pizza_cost3:.2f}")
print(f"Tax: ${sales_tax3:.2f}")
print(f"Delivery: ${delivery_charge3:.2f}")
print(f"Total: ${total3:.2f}")

print()
print(f"Weekend Total: ${weekend_total:.2f}")