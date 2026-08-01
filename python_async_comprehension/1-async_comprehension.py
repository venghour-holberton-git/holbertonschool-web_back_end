#!/usr/bin/env python3
"""Module containing an asynchronous generator."""

import asyncio
import random
from typing import AsyncGenerator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """generate 10 random float and return them all as a list"""
    res_list: List[float] = [num async for num in async_generator()]

    return res_list

if __name__ == "__main__":
    print(asyncio.run(async_comprehension()))
