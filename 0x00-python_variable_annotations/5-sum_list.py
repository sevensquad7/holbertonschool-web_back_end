#!/usr/bin/env python3
"""
sum_list function
"""
from typing import List


def sum_list(input_list : List[float]) -> float:
    """
   return sum of a list floats
    """
    listsum = 0
    for item in input_list:
        listsum+=item;
    return listsum
