#!/usr/bin/env python3
"""
My random wait module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Coroutine that delays for a time and returns the delay time """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
