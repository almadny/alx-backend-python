#!/usr/bin/env python3
"""
Runtime module that contains the runtime function
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension 4 times in parallel with asyncio.gather """
    beg_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - beg_time
