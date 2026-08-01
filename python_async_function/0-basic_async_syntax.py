#!/usr/bin/env python3

"""function module"""


import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """This funtion take in random value, wait then return the value back"""
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

if __name__ == "__main__":
    print(asyncio.run(wait_random(5)))
