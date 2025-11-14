litres = float(input("Enter amount of litres: "))
price_per_litre = 12.50
total_cost = litres * price_per_litre

if litres > 50:
    discount = 0.05 * total_cost
    total_cost -= discount

print(f"Total cost: GHS {total_cost:.2f}")