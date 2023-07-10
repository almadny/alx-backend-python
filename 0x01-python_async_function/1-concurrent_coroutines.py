#!/usr/bin/env python3
"""
Module that spawns the wait random function a given number of times
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ A Function that list and return list of delays """
    co = [asyncio.create_task(await wait_random(max_delay) for i in range(n))]
    delays = await asyncio.gather(*co)
    return sorted(delays)
