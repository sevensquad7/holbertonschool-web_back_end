#!/usr/bin/env python3
"""
wait_n async function
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
   return the list of all the delays (float values)
    """
    ord = await asyncio.gather(*[wait_random(max_delay) for y in range(n)])
    return sorted(ord)
