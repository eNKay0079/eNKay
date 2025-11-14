route = input("Enter a route(Accra to Madina, Accra to Kasoa, Accra to Tema):  ").lower()
passengers = int(input("Enter number of passengers: "))

if route == "accra to madina":
    fare = 5
elif route == "accra to kasoa":
    fare = 10
elif route == "accra to tema":
    fare = 8
else:
    print('Invalid Route')
    fare = 0

total = fare * passengers
print(f"The total fare for {passengers} passengers to {route.title()} is GHS {total}")

