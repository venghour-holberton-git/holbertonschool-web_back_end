#!/usr/bin/env python3

def index_range(page: int, page_size: int):
    return tuple(page * page_size, (page + 1) * page_size)