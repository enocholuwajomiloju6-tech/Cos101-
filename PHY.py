# STUDENT 7 - PHYSICS CALCULATOR

# 1. CALCULATION OF LIFTING WORK
def lifting_work():
    mass = float(input("Enter mass in kg: "))
    height = float(input("Enter height in meters: "))
    gravity = 9.8

    work = mass * gravity * height
    print("Lifting Work =", work, "Joules")


# 2. CALCULATION OF CENTRIPETAL FORCE
def centripetal_force():
    mass = float(input("Enter mass in kg: "))
    velocity = float(input("Enter velocity in m/s: "))
    radius = float(input("Enter radius in meters: "))

    if radius > 0:
        force = (mass * velocity ** 2) / radius
        print("Centripetal Force =", force, "Newtons")
    else:
        print("Radius must be greater than zero")


# 3. CALCULATION OF ELECTRICAL ENERGY
def electrical_energy():
    voltage = float(input("Enter voltage: "))
    current = float(input("Enter current: "))
    time = float(input("Enter time in seconds: "))

    energy = voltage * current * time
    print("Electrical Energy =", energy, "Joules")


# 4. CALCULATION OF SPECIFIC HEAT CAPACITY
def specific_heat():
    heat = float(input("Enter heat energy in Joules: "))
    mass = float(input("Enter mass in kg: "))
    temperature = float(input("Enter temperature change: "))

    if mass != 0 and temperature != 0:
        result = heat / (mass * temperature)
        print("Specific Heat Capacity =", result, "J/kg°C")
    else:
        print("Mass and temperature change cannot be zero")


# 5. CALCULATION OF ESCAPE VELOCITY
def escape_velocity():
    G = 6.674e-11
    mass = float(input("Enter planet mass in kg: "))
    radius = float(input("Enter planet radius in meters: "))

    if mass > 0 and radius > 0:
        velocity = (2 * G * mass / radius) ** 0.5
        print("Escape Velocity =", velocity, "m/s")
    else:
        print("Mass and radius must be positive")


# MAIN PROGRAM
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Lifting Work")
    print("2. Centripetal Force")
    print("3. Electrical Energy")
    print("4. Specific Heat Capacity")
    print("5. Escape Velocity")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        lifting_work()
    elif choice == "2":
        centripetal_force()
    elif choice == "3":
        electrical_energy()
    elif choice == "4":
        specific_heat()
    elif choice == "5":
        escape_velocity()
    else:
        print("Invalid selection. Choose between 1 and 5.")

    answer = input("\nDo you want to perform another operation? (yes/no): ")

    if answer.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
