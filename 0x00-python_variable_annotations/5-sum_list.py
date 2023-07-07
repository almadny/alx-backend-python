#!/usr/bin/env python3
from typing import List
"""
Annotation Project Add Function
"""


def sum_list(input_list: List[float]) -> float:
    """ A function that adds two numbers """

    result: float = 0
    for val in input_list:
        result += val
    return result
