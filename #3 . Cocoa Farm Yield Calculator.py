number_of_bags = int(input("How many bags of cocoa were harvested? "))
price = 8.50
income = number_of_bags * price

if number_of_bags > 100:
    income += 2000

print(f"The total income for {number_of_bags} bags of cocoa is GHS {income}")