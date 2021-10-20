height = input("Enter your height in cm")
weight = input("Enter your weight in kg")

height=float(height)
weight=float(weight)

bmi = weight/(height**2)*10000

print("Bmi Index:")
print(bmi)