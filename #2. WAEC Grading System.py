score = int(input("How much did the student score?(0-100):"))

if score < 0 or score > 100:
    print("Score is Invalid")
elif 100 >= score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
elif score >= 40:
    grade = 'E'
else:
    grade = 'F'

if 0 <= score <= 100:
    print(f"The grade is: {grade}")
