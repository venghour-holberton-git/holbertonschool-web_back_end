#!/usr/bin/env python3
"""
    This is a class module
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Return a List of data from the start index to end index
        """
        assert isinstance(page, int) and page > 0, "Must be int and > 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "Must be int > 0"
        data = self.dataset()
        selected_range = self.index_range(page, page_size)
        return data[selected_range[0]: selected_range[1]]

    def index_range(self, page, page_size):
        """
            Return a tuple of start index and end index
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size

        return (start_index, end_index)
