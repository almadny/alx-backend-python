#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple, TypeVar
"""
A module that defines a function element length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of the input list and its length.
    
    Arguments:
    - lst: A list of strings
    
    Returns:
    - A list of tuples where each tuple contains an element of lst and its length
    """

    return [(i, len(i)) for i in lst]
