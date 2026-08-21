#!/usr/bin/env python3
"""
    This is a function module
"""

def index_range(page, page_size):
    """
        This function return a tuple of start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
