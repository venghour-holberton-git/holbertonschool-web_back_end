#!/usr/bin/env python3

"""function module"""


def sum_list(input_list: list[float]) -> float:
    res: float = 0.0
    for n in input_list:
        res += n
    return res
