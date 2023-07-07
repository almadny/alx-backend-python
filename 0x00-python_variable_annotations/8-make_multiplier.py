#!/usr/bin/env python3
from typing import Callable
"""
Module that contains a function to return another function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""

    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
