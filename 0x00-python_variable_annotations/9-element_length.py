#!/usr/bin/env python3
"""
element_length function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return values con the appropriate types
    """
    return [(i, len(i)) for i in lst]
