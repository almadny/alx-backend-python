#!/usr/bin/env python3
from typing import List, Union
"""
Annotation Project Add Function
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ A function that adds two numbers """

    result: float = 0
    for val in mxd_lst:
        result += val
    return result
