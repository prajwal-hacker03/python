#it is  Trapezoidal Rule:
def my_func(x):
    return 1 / (1 + x**2)

def trapezoidal(x0, xn, n):
    h = (xn - x0) / n
    integration = my_func(x0) + my_func(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration += 2 * my_func(k)

    integration = integration * h / 2
    return integration

# Input from user
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is:", result)


#