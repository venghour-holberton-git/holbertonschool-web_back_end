#!/usr/bin/env python3
"""Module containing the task_wait_n coroutine."""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the delays from n concurrent tasks."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
