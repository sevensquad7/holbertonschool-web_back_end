#!/usr/bin/env python3
"""
safe_first_element function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    return correct duck types annotations
    """
    if lst:
        return lst[0]
    else:
        return None
