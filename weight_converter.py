# Project: Metric-Imperial Converter
# Description: Handles bidirectional conversion between Kgs and Lbs.
# Skills: User Input Handling and Error Prevention.

weight = float(input("Enter your weight: "))
unit = input("Enter unit of weight measurement(kgs/lbs): ")

if unit == "kgs":
    w_converted = weight * 2.205
    print(f"Your weight in lbs is: {round(w_converted)}")
elif unit == "lbs":
    w_converted = weight / 2.205
    print(f"Your weight in kgs is: {round(w_converted)}")
else:
    print(f"Invalid unit: {unit}")
