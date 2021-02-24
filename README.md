# Week 6 workshop: Monte Carlo integration

This week you'll be **pair programming**. Choose one of you to be the driver first; then, every 15 minutes or so, **swap roles**. The driver writes code and shares their screen, the navigator is an active observer/helper.

Work in the script `montecarlo.py`.

## Monte Carlo integration

There are many ways to estimate integrals numerically. In the course, we have been looking at quadrature methods; Monte Carlo integration uses an entirely different approach.

Monte Carlo integration is a numerical method which allows us to approximate definite integrals. The integral of a continuous function f over some interval [a, b] is equal to the **average** of that function over the interval, multiplied by the interval width. The idea is to evaluate the function at many randomly chosen points over [a, b]. Computing the mean of all function evaluations gives an estimate for the integral.

## Task 1

Write a function `monte_carlo(f, a, b, N)` which estimates and returns the integral of a function `f` over some domain [`a`, `b`], by sampling `N` points <img src="https://render.githubusercontent.com/render/math?math=x_i"> chosen randomly in the interval, evaluating <img src="https://render.githubusercontent.com/render/math?math=f%28x_i%29"> at all these points, computing the average of the `N` values, and multiplying the result by `b - a`.

Test your function by defining a function `f()` with a known integral. You can use the example functions in the Week 5 or 6 tutorial sheets for instance.

## Task 2

Using a test function `f()` of your choice, investigate the accuracy of the Monte Carlo method by calculating the error between exact integral and approximation for several values of `N`.

The error should be roughly proportional to <img src="https://render.githubusercontent.com/render/math?math=N^q"> (q is a real number). Can you estimate q?

## Bonus task: Monte Carlo in multiple dimensions

An advantage of this method over those we've seen so far is that the computational cost does not increase as rapidly for higher-dimensional integrals.

Write a function `monte_carlo_2d()` which adapts your `monte_carlo()` function to estimate the integral of a function `f(x, y)` over some finite rectangular domain. You will need to sample `N` points with 2 coordinates each.

How would you approach the same problem on a circular domain?
