#!/usr/bin/env python3

"""
Write a type-annotated function floor which takes a float n as
argument and returns the floor of the float
""" 
import math

def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.
    Arguments:
    n -- A floating-point number

    Returns:
    The largest integer less than or equal to n.
    """
    return math.floor(n)