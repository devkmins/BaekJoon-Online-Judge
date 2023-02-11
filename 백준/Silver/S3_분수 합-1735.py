def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    else:
        return a

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

gcd_value = gcd(B1, B2)
lcm = (B1 * B2) // gcd_value

numerator, denominator = ((lcm // B1) * A1 + (lcm // B2) * A2), lcm

gcd_last_value = gcd(numerator, denominator)

print(numerator // gcd_last_value, denominator // gcd_last_value)
