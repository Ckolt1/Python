budget = float(input("Enter your monthly income: "))

housing = float(
    input("Enter the amount spent on Housing : "))
housing_p = (housing / budget)
utilities = float(
    input("Enter the amount spent on Utilities: "))
utilities_p = (utilities / budget)
groceries = float(
    input("Enter the amount spent on Groceries: "))
groceries_p = (groceries / budget)
transportation = float(
    input("Enter the amount spent on Transportation: "))
transportation_p = (transportation / budget)
healthcare = float(
    input("Enter the amount spent on Health Care: "))
healthcare_p = (healthcare / budget)
personal_care = float(
    input("Enter the amount spent on Personal Care: "))
personal_care_p = (personal_care / budget)
clothing = float(
    input("Enter the amount spent on Clothing: "))
clothing_p = (clothing / budget)
debt = float(
    input("Enter the amount spent on Debt: "))
debt_p = (debt / budget)
# idk how to make the percent appear as a whole number but I give up
print(f"You spend {housing_p} % of your budget on rent")
print(f"You spend {utilities_p}% of your budget on utilities")
print(f"You spend {groceries_p}% of your budget on groceries")
print(f"You spend {transportation_p}% of your budget on transportation")
print(f"You spend {healthcare_p}% of your budget on healthcare")
print(f"You spend {personal_care_p}% of your budget on self care")
print(f"You spend {clothing_p}% of your budget on clothing")
print(f"You spend {debt_p}% of your budget on debt")
