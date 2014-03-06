#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TIES483 - programming assignment

Line Search
- Elimination method
  - bisection
  - goldenSection

- Interpolation methods
?
"""

__author__ = "Mou Hao"
__email__ = "muhaocd@gmail.com"


def bisection (initial_interval, final_length, objectiveFunction, tolerance):
    """
    Bisection method

    input a intial interval, final length, objectiveFunction and tolerance
    output minimizer and iteration times

    >>>minimizer, iteration = bisection([0,1], 0.01, objectiveFunciton,0.005)
    >>>print minimizer, iteration
    >>>0.004, 20
    """

    # intialize
    a = initial_interval[0]
    b = initial_interval[1]
    iteration = 0

    while b - a > final_length :
        x = ( b + a ) / 2.0 - tolerance
        y = ( b + a ) / 2.0 + tolerance        

        if objectiveFunction(x) < objectiveFunction(y) :
            a = a
            b = y
        else :
            a = x
            b = b

        x = ( b + a ) / 2.0 - tolerance
        y = ( b + a ) / 2.0 + tolerance

        iteration = iteration + 1
    
    return (a+b)/2.0, iteration


def goldenSection ():
    pass


if __name__ == '__main__':

	pass

