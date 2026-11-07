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


print("================================================================")
print("                        SciCalc")
print("================================================================")

answers = [] # this is the answers variable
running = True

while running: 
    print("\nWhat do you want to calculate? Enter a number from the list below:")
    print("\n\t1. Speed\t\tv= d / t")
    print("\t2. Acceleration\t\ta = (v2 - v1) / t")
    print("\t3. Force\t\tF= m x a")
    print("\t4. Density\t\tD= m / V")
    print("\t5. Voltage\t\tV= I x R")
    print("\t6. Kinetic Energy\tEk = 0.5 x m x v^2")
    print("\t7. Moles\t\tn = m / M")
    print("\n\t8. Exit SciCalc")
#==============================================
# try elif and else statments for all formulas
#==============================================
    choice = input("\nEnter a number (1-8): ")

    # Stops the program from crashing if the user enters somethign wrong
    try:
        # speed formula
        if choice == "1":
            print("\n----- Speed -----")
            distance = float(input("Distance(m): "))
            time_s = float(input("Time(s): "))
            speed = distance / time_s
            answers.append(f"Speed: {round(speed, 2)} m/s")
            print("Speed =", round(speed, 2), "m/s")

# acceleration formula
        elif choice == "2":
            print("----- Acceleration -----")
            v1 = float(input("Starting Velocity m/s: "))
            v2 = float(input("Final Velocity m/s: "))
            time_s = float(input("Time (s): "))
            acceleration = (v2 - v1) / time_s
            answers.append(f"Acceleration: {round(acceleration, 2)} m/s^2")
            print("Acceleration =", round(acceleration, 2), "m/s^2")
# force formula
        elif choice == "3":
            print("----- Force -----")
            mass = float(input("Mass (kg): "))
            acceleration = float(input("Acceleration (m/s^2): "))
            force = mass * acceleration
            answers.append(f"Force: {round(force, 2)} N")
            print("Force =", round(force, 2), "N")
# density formula
        elif choice == "4":
            print("----- Density -----")
            #mass is going to be written in grams instead of kg
            mass = float(input("Mass (g): "))
            volume = float(input("Volume (cm^3): "))
            density = mass / volume
            answers.append(f"Density: {round(density, 2)} g/cm^3")
            print("Density =", round(density, 2), "g/cm^3")
# voltage formula
        elif choice == "5":
            print("----- Voltage (also known as Ohm's Law) -----")
            current = float(input("Current (A(Amperes)): "))
            resistance = float(input("Resistance (Ω): "))
            vol_tage = current * resistance
            answers.append(f"Voltage: {round(vol_tage, 2)} V")
            print("Voltage =", round(vol_tage, 2), "V")
# kinetic formula
        elif choice == "6":
            print("----- Kinetic Energy -----")
            mass=float(input("Mass (kg): "))
            velocity = float(input("Velocity (m/s): "))
            energy = 0.5 * mass * velocity ** 2
            answers.append(f"Kinetic Energy: {round(energy, 2)} J")
            print("Kinetic Energy =", round(energy, 2), "J")
# moles formula
        elif choice == "7":
            print("----- Moles -----")
            mass = float(input("Mass (g): "))
            molar_mass = float(input("Molar mass (g/mol): "))
            moles = mass / molar_mass
            answers.append(f"Moles: {round(moles, 2)} mol")
            print("Moles =", round(moles, 2), "mol")
# exit option
        elif choice == "8":
            #Gives the answers that the program has calculated in that session and then exits the program
            print("\n================ YOUR ANSWERS ==================")
            print("\n".join(answers))
            print("================================================")
            print("Thanks for using SciCalc!!! GoodBYE!")


            running = False

        else: 
            print("That is not an option. Please PICK 1-8.")

# this program happens when the user types a letter instead of a number
    except ValueError:
        print("N00000!! Please type numbers only.")

# happens when the user divides by 0 basically gives an error
    except ZeroDivisionError:
        print("N00000!! You cannot divide by 0 (zero).")