def my_func(x):
    return 1 / (1 + x**2)

def simpson13(x0, xn, n):
    h = (xn - x0) / n
    integration = my_func(x0) + my_func(xn)
    k = x0

    for i in range(1, n):
        k += h
        if i % 2 == 0:
            integration = integration + 2 * my_func(k)
        else:
            integration = integration + 4 * my_func(k)

    integration = integration * h / 3
    return integration

lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals (must be even): "))

if sub_interval % 2 != 0:
    print("Error: Simpson's 1/3 rule requires an even number of sub-intervals.")
else:
    result = simpson13(lower_limit, upper_limit, sub_interval)
    print("Integration result by Simpson's 1/3 method is: %0.6f" % result)