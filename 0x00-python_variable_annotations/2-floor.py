#!/usr/bin/env python3


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.
    Arguments:
    n -- A floating-point number

    Returns:
    The largest integer less than or equal to n.
    """
    return int(n) if n >= 0 else int(n - 1)