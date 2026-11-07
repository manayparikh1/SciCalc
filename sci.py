'''
File: sci.py
Date: 2026-Nov-07

Description: This will be a easy program that will calculate a few things in the branch
of science using a few formulas. The user will be prompted to enter what they want to calculate
out of the options given. The user will then have to prompt the values based on the equation they choose.

They are very simple formulas that are used in science.

Formulas:

Speed (v = d / t)
Acceleration (a = (v2 - v1) / t)
Force (F = m * a)
Density (D = m / V)
Voltage (V = I * R)
Kinetic Energy (Ek = 1/2*m*v²)
Moles (n = m / M)

'''


print("=======================================")
print("                SciCalc")
print("=======================================")

running = True

while running: 
    print("\nWhat do you want to calculate?")
    print("\t1. Speed\t\tv= d / t")
    print("\t2. Acceleration\t\ta = (v2 - v1) / t")
    print("\t3. Force\t\tF= m x a")
    print("\t4. Density\t\tD= m / V")
    print("\t5. Voltage\t\tV= I x R")
    print("\t6. Kinetic Energy\t\tEk = 0.5 x m x v^2")
    print("\t7. Moles\t\tn = m / M")
    print("\t8. Exit SciCalc")
#==============================================
# try elif and else statments for all formulas
#==============================================
    choice = input("Enter a number (1-8): ")

    # Stops the program from crashing if the user enters somethign wrong
    try:
        if choice == "1":
            print("\n--- Speed ---")
            distance = float(input("Distance(m): "))
            time_s = float(input("Time(s): "))
            speed = distance / time_s
            print("Speed =", round(speed, 2), "m/s")

        elif choice == "2":
            print("\n--- Acceleration ---")
            v1 = float(input("Starting Velocity m/s: "))
            v2 = float(input("Final Velocity m/s: "))
            time_s = float(input("Time (s): "))
            acceleration = (v2 - v1) / time_s
            print("Acceleration =", round(acceleration, 2), "m/s^2")



    
