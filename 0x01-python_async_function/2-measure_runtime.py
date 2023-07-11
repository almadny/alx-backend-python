#!/usr/bin/env python3
""""
Module containing measure time function
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Calculates the average time a coroutine takes to execute
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapsed = end - start
    total_time = elapsed / n
    return total_time
