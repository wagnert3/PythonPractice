# BMI Calculator with Conditional Statements

print("Welcome to the BMI Calculator!")

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
    
print("Thank you for using the BMI Calculator!")

