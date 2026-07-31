#!/usr/bin/env python3

"""function module"""


from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    return (k, v*v)
