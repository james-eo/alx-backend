#!/usr/bin/env python3
"""This module contains a pagination function with
start and end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function to paginate a page with indexes.

    Args:
        page: A section of a dataset.
        page_size: The number of items in each page section

    Returns:
        A tuple of size two containing a start index and an end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
