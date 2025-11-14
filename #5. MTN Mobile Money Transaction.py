amount = float(input("How much to be sent?: "))

if amount <= 100:
    charge = 2
elif amount <= 500:
    charge = 5
else:
    charge = 10

received_amount = amount - charge
print(f"Amount sent: GHS {amount}")
print(f"Transaction charge: {charge}")
print(f"Amount received: {received_amount}")