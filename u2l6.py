import math

# Print table header
print(f"{'N':>3}|{'SQR':>5}|{'Cubes':>7}|{'Roots':>5}")
print("---+-----+-------+-----")

# Loop through values from 10 to 200, step 15
for N in range(10, 201, 15):
    SQR = N ** 2
    Cubes = N ** 3
    Roots = math.sqrt(N)
    print(f"{N:3}|{SQR:5}|{Cubes:7}|{Roots:5.2f}")
