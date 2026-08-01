#!/usr/bin/env python3
"""Module containing the wait_n coroutine."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Spawn wait_random n times and return the delays in ascending order."""
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    return (end_time - start_time) / n

if __name__ == "__main__":
    print(asyncio.run(measure_time(3, 4)))
