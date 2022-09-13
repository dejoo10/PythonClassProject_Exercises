import sys


def conver_gal(lit):
    conversion = 3.7854 * lit
    return conversion

fuel = int(input("Enter the volume of your gasoline in gallons:.."))
print(f"{conver_gal(fuel):.2f} liters" )

sys.exit(0)