#!/usr/bin/env python3
"""Module that measures the average execution time of an asynchronous coroutine."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time required to execute the wait_n coroutine."""
    start: float = time.perf_counter()
    await wait_n(n, max_delay)
    return (time.perf_counter() - start) / n
