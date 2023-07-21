#!/usr/bin/env python3
"""Helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a suple of size two containing \
        a stert and end index"""
    start = (page - 1) * page_size
    return (start, start + page_size)
