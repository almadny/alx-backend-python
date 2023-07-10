#!/usr/bin/env python3
"""
Module that spawns the wait random function a given number of times
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ A Function that list snd return list of delays """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    delays.sort()
    return delays
