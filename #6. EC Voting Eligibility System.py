name = input("What is your name? : ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()

if age >= 18 and nationality == 'ghanaian':
    print(f"You are eligible to vote.")
else:
    print(f"You are not eligible to vote.")
