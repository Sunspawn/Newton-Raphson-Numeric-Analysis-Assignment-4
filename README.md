# Newton-Raphson-Numeric-Analysis-Assignment-4

## About

The Newton-Raphson and secant methods for finding the root of a function.

## The bad

Uses sympy to "parse" the user input into a function, meaning it is not very safe. Also, something goes wrong when I try to run logarithmic functions through the NR method, suggesting something is not kosher with the interaction of eval() (which sympy uses) and scipy's derivative() function, since that's the only difference between the two methods.

No, I have no clue how to fix it. /endrant
