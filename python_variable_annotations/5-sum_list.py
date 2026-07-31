#!/usr/bin/env python3

"""function module"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """return a float"""
    res: float = 0.0
    for n in input_list:
        res += n
    return res
