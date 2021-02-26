import numpy as np
import matplotlib.pyplot as plt

# Task 1

def f(x):
    return np.sin(x)

def monte_carlo(f, a, b, N):
    '''
    Returns a Monte Carlo approximation of the integral
    of f(x) over [a, b], using N points.
    '''
    # Generate N random points in the interval
    x = (b - a) * np.random.random(N) + a

    # Compute and return the approx. integral of f(x)
    return (b - a) * np.mean(f(x))

# Test the function
a, b = 0, np.pi
I_exact = 2
I_approx = monte_carlo(f, a, b, 1000)
print(I_exact, I_approx)

# Task 2: estimate the error.
# We test 20 logarithmically spaced values of N
# between 10 and 10 million.
err = []
N_vals = np.logspace(1, 7, 20, dtype=int)
for N in N_vals:
    I_approx = monte_carlo(f, a, b, N)
    err.append(abs(I_exact - I_approx))

fig, ax = plt.subplots()
ax.plot(np.log(N_vals), np.log(err), 'rx')
ax.set(title='Error for Monte Carlo integration',
       xlabel=r'$\log(N)$',
       ylabel=r'$\log(E)$')
plt.show()

# Estimate q using linear regression (see Video 2 week 6)
q = np.polyfit(np.log(N_vals), np.log(err), 1)[0]
print(f'The error is proportional to N^{q:.2f}.')

# q = -0.5 indicates that the error is proportional to 1/sqrt(N).
# This means that to divide the error by 2, we have to use 4 times as many sample points.


# Bonus task

def monte_carlo_2d(f, a, b, N):
    '''
    Returns a Monte Carlo approximation of the integral
    of f(x, y) for x in [a[0], b[0]], and y in [a[1], b[1]]
    using N points.
    '''
    # Generate N random points in the rectangle
    x = (b[0] - a[0]) * np.random.random(N) + a[0]
    y = (b[1] - a[1]) * np.random.random(N) + a[1]

    # Compute and return the approx. integral of f(x, y)
    return (b[0] - a[0]) * (b[1] - a[1]) * np.mean(f(x, y))


# Test the function
def f(x, y):
    return x * y

a, b = [0, 0], [1, 1]
I_exact = 1/4
I_approx = monte_carlo_2d(f, a, b, 1000)
print(I_exact, I_approx)
