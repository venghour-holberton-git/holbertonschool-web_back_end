#!/usr/bin/env python3

"""function module"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """this function return a List of tuple of squence"""
    return [(i, len(i)) for i in lst]
