# python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit of measurement (L for pounds, K for kilograms): ")

if unit == "k":
    weight = weight * 2.20462
    print(f"Your weight is {round(weight, 2)} pounds")
elif unit == "L":
    weight = weight / 2.20462
    print(f"your weight is {round(weight, 2)} kilograms")
else:
    print("Invalid unit of measurement")
