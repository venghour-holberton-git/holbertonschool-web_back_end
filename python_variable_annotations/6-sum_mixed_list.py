#!/usr/bin/env python3

"""function module"""


from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """return a float"""
    res: float = 0.0
    for n in mxd_lst:
        res += n
    return res
