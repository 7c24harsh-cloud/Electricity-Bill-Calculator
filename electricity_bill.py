# Electricity Bill Calculator
# Project No. 95

# Function 1: Calculate Energy Charge

def calculate_energy_charge(units):

    if units <= 100:
        energy = units * 3

    elif units <= 200:
        energy = (100 * 3) + ((units - 100) * 5)

    else:
        energy = (100 * 3) + (100 * 5) + ((units - 200) * 8)

    return energy


# Function 2: Generate Electricity Bill

def generate_bill(name, units):

    # Calculate energy charge
    energy = calculate_energy_charge(units)

    # Fixed charge
    fixed = 50

    # Calculate tax (5%)
    tax = (energy + fixed) * 0.05

    # Calculate total bill
    total = energy + fixed + tax

    # Print formatted electricity bill
    print("\n================================")
    print("       ELECTRICITY BILL")
    print("================================")

    print("Consumer Name :", name)
    print("Units Consumed:", units)

    print("--------------------------------")
    print("Energy Charge : Rs.", format(energy, ".2f"))
    print("Fixed Charge  : Rs.", format(fixed, ".2f"))
    print("Tax (5%)      : Rs.", format(tax, ".2f"))

    print("--------------------------------")
    print("Total Bill    : Rs.", format(total, ".2f"))
    print("================================")


# Main Program

print("WELCOME TO ELECTRICITY BILL CALCULATOR")

# Take consumer name
name = input("Enter Consumer Name: ")

# Take electricity units
try:
    units = float(input("Enter Units Consumed: "))

    # Check invalid input
    if units < 0:
        print("Invalid units. Enter a non-negative number.")

    else:
        generate_bill(name, units)

except ValueError:
    print("Invalid units. Enter a non-negative number.")