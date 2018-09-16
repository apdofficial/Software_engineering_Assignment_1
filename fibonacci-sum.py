# Andrej Pistek
# 450966
# Multiples of 3 and 5 up to 10000

a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b  # the real formula for Fibonacci sequence
print(total)