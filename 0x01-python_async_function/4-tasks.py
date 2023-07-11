#!/usr/bin/env python3
"""
Module containing task_wait_n
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that create tasks and add them to even loop  """
    rout = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*rout)
    return sorted(delays)
