def gcd(a,b):
	if b != 0:
	b = a % b
	a = b
    elif b == 0:
        return a
    gcd(b, a % b)


