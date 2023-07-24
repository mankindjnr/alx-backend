#!/usr/bin/env python3
"""
write a function named index_range that takes two
integer arguments page and page_size.
"""
import csv
import math
from pprint import pprint
from typing import List, Tuple, Dict, Union


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

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Union[int, str, List[List[str]], None]]:
        """return a dictionary contianing key value pairs"""
        indexes = index_range(page, page_size)
        start, end = indexes[0], indexes[1]
        data_size = len(self.dataset())
        dataset = self.dataset()

        total_pages = math.ceil(data_size / page_size)

        if start >= data_size:
            return {
                'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
            }

        data = dataset[start:end]
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
