savings = {
    'Akosua': 200,
    'Ama': 150,
    'Adwoa': 300
}

print("Current savings:")
for name, amount in savings.items():
    print(f"Name: {name}, Amount: GHS {amount}")

name = input("Enter trader's name: ")

if name in savings:
    deposit = float(input(f"Enter amount deposited by {name}: "))
    savings[name] = savings[name] + deposit
    print("Updated savings:")
    for name, amount in savings.items():
        print(f"Name: {name}, Amount: GHS {amount:.2f}")
else:
    print(f"{name} doesn't exist in records.")