#!/usr/bin/env python3
"""
write a function named index_range that takes two
integer arguments page and page_size.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """calculating start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + (page_size)

    return (start_index, end_index)


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
        """ind the correct indexes to paginate the dataset"""
        indexes = index_range(page, page_size)
        if indexes is not None:
            start = indexes[0]
            end = indexes[1]
            data = self.dataset()

            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0

            pages = []
            try:
                for item in range(start, end):
                    pages.append(data[item])

                return pages
            except IndexError:
                return pages
