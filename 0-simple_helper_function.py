#!/usr/bin/env python3
"""
write a function named index_range that takes two
integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """calculating start and end index"""
    if page <= 0 or page_size <= 0:
        return

    start_index = (page - 1) * page_size
    end_index = start_index + (page_size)

    return (start_index, end_index)
