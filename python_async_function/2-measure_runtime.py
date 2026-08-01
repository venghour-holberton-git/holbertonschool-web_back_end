#!/usr/bin/env python3
"""Module containing the wait_n coroutine."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Spawn wait_random n times and return the delays in ascending order."""
    start_time: float = time.perf_counter()
    await wait_n(n, max_delay)
    end_time: float = time.perf_counter()
    total_time: float = end_time - start_time
    return total_time / n
