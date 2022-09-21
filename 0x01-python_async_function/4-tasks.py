#!/usr/bin/env python3
"""
wait_n async function
"""
import asyncio
from typing import List


task_wait_random = __import__('1-concurrent_coroutines').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list
    """
    od = await asyncio.gather(*[task_wait_random(max_delay) for y in range(n)])
    return sorted(od)
