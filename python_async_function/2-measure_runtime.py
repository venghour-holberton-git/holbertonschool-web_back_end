#!/usr/bin/env python3
"""Module containing the wait_n coroutine."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n."""
    start: float = time.perf_counter()
    await wait_n(n, max_delay)
    return (time.perf_counter() - start) / n
