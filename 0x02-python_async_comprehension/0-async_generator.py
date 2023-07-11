#!/usr/bin/env python3
"""
Module Containing async_generator coroutine
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that creates an iterator
    """
    for i in range(10):
        await asyncio.sleep(1)
        randNum = random.uniform(0, 10)
        yield randNum
