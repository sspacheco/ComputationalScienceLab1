from decimal import Decimal, getcontext
import math
import matplotlib.pyplot as plt


getcontext().prec = 110

r = Decimal(input("Enter sphere radius: "))

pi_truncate = Decimal("3.1415")
pi_rounding = Decimal("3.1416")

pi_t20 = Decimal("3.14159265358979323846")
pi_t40 = Decimal("3.1415926535897932384626433832795028841971")
pi_t60 = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
pi_t100 = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")

pi_r20 = Decimal("3.14160000000000000000")
pi_r40 = Decimal("3.1416000000000000000000000000000000000000")
pi_r60 = Decimal("3.141600000000000000000000000000000000000000000000000000000000")
pi_r100 = Decimal("3.1416000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")


ssa_piTruncate = Decimal(4) * pi_truncate * r*r
ssa_piRounding = Decimal(4) * pi_rounding * r*r

ssa_pit20 = Decimal(4) * pi_t20 * r*r
ssa_pit40 = Decimal(4) * pi_t40 * r*r
ssa_pit60 = Decimal(4) * pi_t60 * r*r
ssa_pit100 = Decimal(4) * pi_t100 * r*r

ssa_pir20 = Decimal(4) * pi_r20 * r*r
ssa_pir40 = Decimal(4) * pi_r40 * r*r
ssa_pir60 = Decimal(4) * pi_r60 * r*r
ssa_pir100 = Decimal(4) * pi_r100 * r*r

print(f"Sphere Surface Area (Radius: {r})\n")
print("Truncated Pi: ", pi_truncate)
print("Surface Area: ", ssa_piTruncate)
print("Rounded Pi: ", pi_rounding)
print("Surface Area: ", ssa_piRounding)
print("Difference :", ssa_piRounding - ssa_piTruncate)

print("\nPrecision: 20 digits")
print("Truncated Pi: ", pi_t20)
print("Surface Area: ", ssa_pit20)
print("Rounded Pi: ", pi_r20)
print("Surface Area: ", ssa_pir20)
print("Difference :", ssa_pir20 - ssa_pit20)

print("\nPrecision: 40 digits")
print("Truncated Pi: ", pi_t40)
print("Surface Area: ", ssa_pit40)
print("Rounded Pi: ", pi_r40)
print("Surface Area: ", ssa_pir40)
print("Difference :", ssa_pir40 - ssa_pit40)

print("\nPrecision: 60 digits")
print("Truncated Pi: ", pi_t60)
print("Surface Area: ", ssa_pit60)
print("Rounded Pi: ", pi_r60)
print("Surface Area: ", ssa_pir60)
print("Difference :", ssa_pir60 - ssa_pit60)

print("\nPrecision: 100 digits")
print("Truncated Pi: ", pi_t100)
print("Surface Area: ", ssa_pit100)
print("Rounded Pi: ", pi_r100)
print("Surface Area: ", ssa_pir100)
print("Difference :", ssa_pir100 - ssa_pit100)

labels = ["3.1415/3.1416", "20d", "40d", "60d", "100d"]

truncate_values = [
    float(ssa_piTruncate),
    float(ssa_pit20),
    float(ssa_pit40),
    float(ssa_pit60),
    float(ssa_pit100)
]

rounded_values = [
    float(ssa_piRounding),
    float(ssa_pir20),
    float(ssa_pir40),
    float(ssa_pir60),
    float(ssa_pir100)
]

plt.plot(labels, truncate_values, marker='o', label="Truncated π")
plt.plot(labels, rounded_values, marker='s', label="Rounded π")

plt.xlabel("π Precision")
plt.ylabel("Sphere Surface Area")
plt.title("Effect of π Approximation on Sphere Surface Area")
plt.legend()
plt.grid(True)
plt.ticklabel_format(useOffset=False, axis='y')

plt.show()
