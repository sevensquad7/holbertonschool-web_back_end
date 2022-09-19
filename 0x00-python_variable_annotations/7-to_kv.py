#!/usr/bin/env python3
"""
to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a string and a number
    """
    return (k, v * v)
