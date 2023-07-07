#!/usr/bin/env python3
from typing import Union, Tuple
"""
Annotation Project Add Function
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that adds two numbers """

    result = (k, v**2)
    return result
