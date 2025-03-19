import pytest
from main import bmi_calculator

@pytest.mark.parametrize("feet, inches, weight, expected_bmi, expected_category", [

    #Normal Test Cases

    #Underweight Test
    (6, 2, 100, 13.15, "Underweight"),
    #Normal Weight Test
    (5, 2, 130, 24.35, "Normal Weight"),
    #Overweight Test
    (3, 2, 60, 29.92, "Overweight"),
    #Obese Test
    (4, 2, 200, 57.6, "Obese"),



    #Boundry Shift Test Case

    #Exact boundary between Underweight & Normal
    (5, 6, 111.5, 18.43, "Underweight"),

    #Exact boundary between Normal and Overweight
    (5, 6, 151.28, 25.0, "Overweight")



])
def test_bmi_calculator(feet, inches, weight, expected_bmi, expected_category):
    bmi, category = bmi_calculator(feet, inches, weight)
    assert bmi == expected_bmi, f"Expected BMI was {expected_bmi}, what was calculated {bmi}"
    assert category == expected_category, f"Expected {expected_category}, what was calculated {category}"