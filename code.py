"""Assignment 5 for Numeric Analysis

Nikolay Babkin 321123242

Newton-Raphson and the secant method"""

from scipy.misc import derivative
from sympy import *


epsilon = 1e-10
max_iterations = 100


def read_func():
    """Reads a mathematical function with an x variable from the user.
    :return:                The function
    """
    input_string = input(">> Enter a function using python syntax:\n>> ")
    expr = sympify(input_string)
    x = var('x')
    return lambda a: expr.subs(x, a)


def deriv(f):
    """Gives a derivative function of f.
    :param f:               The function to differentiate.
    :return:                The derivative function.
    """
    return lambda x: derivative(f, x, dx=epsilon)


def newton_raphson(f, start, end, error=epsilon, max_iter=max_iterations):
    """Finds an approximation of a root of the given polynomial within the
range provided by the user, using the Newton-Raphson method.
    :param f:            The polynomial function that receives x and returns f(x).
    :param start:           The lower bound of the range.
    :param end:             The upper bound of the range.
    :param error:           The error margin to adhere to.
    :param max_iter:        The maximum amount of iterations.
    :return:                A tuple with the guess and a flag that says whether
 the method was able to converge or not.
    """
    # differentiate f for start
    df = deriv(f)
    # first guess will be smack in the middle of the
    guess = (end - start) / 2 + start
    i = 1
    cont = True
    good = True

    print("Newton-Raphson method")

    while cont and good:
        # print the number of the iteration and the result it reached so far
        print('Iteration #%d: Xi = %f, f(Xi) = %f' % (i, guess, f(guess)))
        i += 1

        # calculate new guess using the newton-raphson formula
        guess = guess - f(guess) / df(guess)

        # check if the value of f at the new guess is close enough to 0
        cont = abs(f(guess)) > error

        # check if still in range
        good = i < max_iter

    # print the result of the final iteration
    print('Iteration #%d: Xi = %f, f(Xi) = %f' % (i, guess, f(guess)))

    # return the final guess
    return guess, good


def secant_method(f, start, end, error=epsilon, max_iter=max_iterations):
    """Find the root of a function using the secant method.
    :param f:               The polynomial function that receives x and returns f(x).
    :param start:           The lower bound of the range.
    :param end:             The upper bound of the range.
    :param error:           The error margin to adhere to.
    :param max_iter:        The maximum amount of iterations.
    :return:                A tuple with the root and whether the method
 was able to converge or not.
    """
    guess1 = start + (end - start) / 3
    guess2 = start + 2 * (end - start) / 3
    i = 1

    print("Secant method")

    while abs(f(guess2)) > error and i < max_iter:
        # print the number of the iteration and the result it reached so far
        print('Iteration #%d: Xi-1 = %f, Xi = %f, f(Xi) = %f' % (i, guess1, guess2, f(guess2)))
        i += 1

        # get new guesses
        guess1, guess2 = guess2, (guess1 * f(guess2) - guess2 * f(guess1)) / (f(guess2) - f(guess1))

    return guess2, i < max_iter


if __name__ == "__main__":
    f = read_func()

    result = newton_raphson(f, 1, 5)
    print('The result was: x = %0.6f and f(x) = %0.6f\n' % (result[0], f(result[0])))

    result = secant_method(f, 1, 5)
    print('The result was: x = %0.6f and f(x) = %0.6f' % (result[0], f(result[0])))
