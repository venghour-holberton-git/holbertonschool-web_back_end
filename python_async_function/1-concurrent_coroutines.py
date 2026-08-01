#!/usr/bin/env python3

"""function module"""


import asyncio
import random
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function get n and max delay"""
    float_list: List[float] = []
    for i in range(n):
        float_list.append(await wait_random(max_delay))
    return float_list

if __name__ == "__main__":
    print(asyncio.run(wait_n(3, 5)))
