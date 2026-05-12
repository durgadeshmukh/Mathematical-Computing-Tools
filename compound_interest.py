# Project: Compound Interest Calculator
# Description: Calculates future value of investments using principal, rate, and time.
# Skills: Mathematical Modeling and Floating-Point Arithmetic.

principle = float(input("Enter principle value: "))
rate = float(input("Enter rate value: "))
time = int(input("Enter number of years: "))

if principle <= 0:
    print("Invalid value!")
elif rate <= 0:
    print("Invalid value!")
elif time <= 0:
    print("Invalid value!")
else:
    I = principle * pow((1 + (rate/100)), time)
    print(f"Value of interest for {principle} rupees with rate {rate}% in {time} years is: ₹{round(I,2)}") 