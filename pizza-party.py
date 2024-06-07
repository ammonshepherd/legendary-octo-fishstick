# Week 4. Problem 2: Pizza Party

import math

people = int(input("Number of people: "))
slices_per_person = float(input("Number of slices/person: "))
one_pizza_cost = float(input("Cost of one pizza: "))

slices_per_pizza = 8

slices_needed = people * slices_per_person

pizzas_needed = math.ceil(slices_needed / slices_per_pizza)

pizza_cost = one_pizza_cost * pizzas_needed

sales_tax = pizza_cost * 0.07
delivery_charge = (pizza_cost + sales_tax) * 0.2

total = pizza_cost + sales_tax + delivery_charge

print()
print("Friday Night Party")
print(f"{pizzas_needed} Pizzas: ${pizza_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Delivery: ${delivery_charge:.2f}")
print(f"Total: ${total:.2f}")