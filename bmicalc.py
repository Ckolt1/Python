
global  pounds_to_kilograms
pounds_to_kilograms = 0.453592
global  inches_to_meters
inches_to_meters = .0254

def formula_bmi(weightpds,heightin):
    # covert to metric
    weightmetric = weightpds * pounds_to_kilograms
    heightmetric = heightin * inches_to_meters

    #bmi = weight / (height * height)
    bmi = weightmetric / (heightmetric * heightmetric)
    return bmi
def bmi_range(bmi):
    if bmi < 18.5:
        return "You are underweight"
    elif 19 <= bmi < 25:
        return "you are a normal weight"
    elif 26 <= bmi < 30:
        return "You are overweight"
    else:
        return "You are obese, lay off the snacking"

def main():
    # convert to float to handle the data
    weightpds = float(input("Enter your weight(pds): "))
    heightin = float(input("Enter your height(in): "))

    bmi = formula_bmi(weightpds, heightin)

    range = bmi_range(bmi)

    print(f"Your BMI is {bmi:.3f}. {range}.")
main ()