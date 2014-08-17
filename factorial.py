#! /usr/bin/python


def factorial(n):
    if n < 2:
        return  1
    f = 1
    while n >= 2:
        f *= n
        n -= 1
        print(f),
    return f

print(factorial(5))
