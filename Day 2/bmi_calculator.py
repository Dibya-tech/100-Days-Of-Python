# Asks the user for their height and weight as input and prints their BMI

height = float(input("Enter height in mtr\n"))
weight = float(input("Enter weight in kg\n"))

bmi = weight / pow(height, 2)

print("Your BMI is - " + str(int(bmi)))
