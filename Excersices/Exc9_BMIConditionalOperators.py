##BMIConditionalOperator
weight = float(input("Enter your weight in kg "))
height = float (input("Enter your height in metres "))
BMI = weight/(height*height)
print("BMI :",round(BMI,2))
if(BMI <= 18.5):
    print("Underweight")
elif((BMI > 18.5) and (BMI <= 24.9)):
    print("Normal weight")
elif((BMI > 24.9) and (BMI <= 29.9)):
    print("Overweight")
elif(BMI >= 30):
    print("Obesity")
