import pytest
from main import bmi_calculator

@pytest.mark.parametrize("feet, inches, weight, expected_bmi, expected_category", [

    #Normal Test Cases

    #Underweight Test
    (6, 2, 100, 13.1, "Underweight"),
    #Normal Weight Test
    (5, 2, 130, 24.3, "Normal Weight"),
    #Overweight Test
    (3, 2, 60, 29.9, "Overweight"),
    #Obese Test
    (4, 2, 200, 57.6, "Obese"),



    #Boundry Shift Test Case

    # **Normal Weight Boundary Tests**
    (1, 0, 3.68, 18.4, "Underweight"), #OFF Lower Boundary
    (1, 0, 3.7, 18.5, "Normal Weight"), #ON Lower Boundary
    (1, 0, 3.73, 18.6, "Normal Weight"), #OFF Lower Boundary
    (1, 0, 4, 20, "Normal Weight"), #Interior
    (1, 0, 4.98, 24.9, "Normal Weight"), #OFF Upper Boundary
    (1, 0, 5, 25, "Overweight"), #ON Upper Boundary
    (1, 0, 5.03, 25.1, "Overweight"), #OFF Upper Boundary

    # **Overweight Boundary Tests**
    (1, 0, 5.7, 28.5, "Overweight"), #Interior
    (1, 0, 5.98, 29.9, "Overweight"), #OFF Upper Boundary
    (1, 0, 6, 30, "Obese"), #ON Upper Boundary
    (1, 0, 6.03, 30.1, "Obese") #OFF Upper Boundary

])
def test_bmi_calculator(feet, inches, weight, expected_bmi, expected_category):
    bmi, category = bmi_calculator(feet, inches, weight)
    assert bmi == expected_bmi, f"Expected BMI was {expected_bmi}, what was calculated {bmi}"
    assert category == expected_category, f"Expected {expected_category}, what was calculated {category}"