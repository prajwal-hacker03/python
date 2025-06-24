def simpsons_3_8_rule(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 3):
        s += 3 * f(a + i * h)
    for i in range(3, n, 3):
        s += 2 * f(a + i * h)
    for i in range(2, n, 3):
        s += 3 * f(a + i * h)
    return s * 3 * h / 8

def f(x):
    return 1 / (1 + x**2)

a = 0
b = 6
n = 6
result = simpsons_3_8_rule(f, a, b, n)
print('%3.5f' % result)
