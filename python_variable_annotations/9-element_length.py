#!/usr/bin/env python3

"""function module"""

from typing import Union, List, Tuple


def element_length(lst: List[List[int]]) -> List[Tuple[List[int], int]]:
    return [(i, len(i)) for i in lst]
