# Project: Digital Countdown Utility
# Description: A time-management tool with live updates.
# Skills: Time Module and System-Level Loops.

import time
t = int(input("Enter time in seconds: "))

for x in range(t,0,-1):
    print(x)
    time.sleep(1)
print("Wake Up!!")
