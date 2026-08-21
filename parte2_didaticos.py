import numpy as np

def f(x):
    return x**3 - 9*x + 3

x = np.linspace(-5, 5, 11)

for xi in x:
    print(xi, f(xi))