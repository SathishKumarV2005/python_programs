#BMI calculator

weight=float(input("enter the weight in kg:"))
height=float(input("enter the height in m:"))

bmi=weight/(height**2)

if bmi<=18.4:
     print("underweight") 
elif bmi<=24.9:
     print("normal")
elif bmi<=39.9:
    print("overweight ")
else:
     print("obese")
