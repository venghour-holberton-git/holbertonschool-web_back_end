#!/usr/bin/env python3

def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


if __name__ == "__main__":
    print(index_range(3, 5))
