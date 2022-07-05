a, b = map(int, input().split())

if a % b == 0:
    gcd = min(a, b)
else:
    if a >= b:
        gcd = a % b
    else:
        gcd = b % a
lcm = a * b // gcd

print(gcd)
print(lcm)