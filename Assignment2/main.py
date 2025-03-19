#BMI Calculator
def bmi_calculator(feet, inch, pound):

    weight_kg = pound * 0.45
    #turn feet into inches
    height = (feet*12) + inch
    height_m = height * 0.025
    total_height = height_m ** 2
    bmi = weight_kg/total_height

    if bmi < 18.5 :
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2) , category

def main():
    print("BMI CALCULATOR")
    try:
        print("Enter your height")
        feet = int(input("Feet: "))
        inch = int(input("Inches: "))
        print("Enter your Weight")
        pound = float(input("lbs: "))

        bmi, category = bmi_calculator(feet, inch, pound)
        print(f"Your total BMI is {bmi}")
        print(f"You are categorized as: {category}")


    except ValueError:
        print("Please input a valid value.")

if __name__=="__main__":
    main()