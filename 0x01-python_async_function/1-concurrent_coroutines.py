#!/usr/bin/env python3
"""
Module that spawns the wait random function a given number of times
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ A Function that list snd return list of delays """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return delays
