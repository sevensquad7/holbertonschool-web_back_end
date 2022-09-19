#!/usr/bin/env python3
"""
make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return multiplier
    """
    def float_multiplier(m: float) -> float:
        """
        return float_multiplier
        """
        return m * multiplier
    return float_multiplier
