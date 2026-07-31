#!/usr/bin/env python3

"""function module"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing the string and the square of the number."""
    return (k, v*v)
