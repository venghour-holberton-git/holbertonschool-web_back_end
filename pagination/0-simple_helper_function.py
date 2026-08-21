#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple:
    return ((page - 1) * page_size, page * page_size)


if __name__ == "__main__":
    print(index_range(3, 5))
