#1
def bmi(height, weight):
    bmi = round(weight / ((height/100)**2), 1)

    if bmi > 30:
        body = "Obese"
    elif 25 <= bmi <= 30:
        body = "Overweight"
    elif 18.5 <= bmi <= 24.9:
        body = "Normal"
    elif bmi < 18.5:
        body = "Underweight"

    return bmi, body


usr = input().split(", ")
height = int(usr[0])
weight = int(usr[1])
result = bmi(height, weight)
print(f"Score is {result[0]}, You are {result[1]}")