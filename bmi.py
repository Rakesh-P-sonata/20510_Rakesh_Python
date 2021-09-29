height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
print(f"You BMI is {BMI} \n")
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy weight.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are highly over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are highly obese.")
