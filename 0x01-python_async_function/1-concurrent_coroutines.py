#!/usr/bin/env python3
""""
Module containing wait_n function
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that runs a given coroutine for an amount of time"""

    rout = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*rout)
    return sorted(delays)
