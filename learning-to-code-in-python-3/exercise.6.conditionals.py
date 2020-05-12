#!/usr/bin/env python3

weight = float( input("How much do you weight (kg)?: ") )
height = float( input("How tall are you (m)?: ") )

bmi = weight / (height * height)

if ( bmi <= 18.5 ):
    assessment = 'under weight'
elif (bmi > 18.5) and (bmi <= 24.9):
    assessment = 'normal weight'
elif (bmi > 24.9 and bmi <= 29.9):
    assessment = 'overweight'
else:
    assessment = 'obese'
    
print(f"Your BMI is {round(bmi, 2)}. You're classified as {assessment}.")