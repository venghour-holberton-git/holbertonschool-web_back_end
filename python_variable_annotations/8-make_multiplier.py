#!/usr/bin/env python3

"""function module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""

    def multiply(value: float) -> float:
        """Multiply a float by the captured multiplier."""
        return value * multiplier

    return multiply