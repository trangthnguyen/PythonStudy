#!/usr/bin/env python3
def fibRecur(n):
    """Assumes n an int >= 0
        Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)
