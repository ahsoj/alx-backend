#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination
"""
import csv

# import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return dictionary containing\
                index: int
                next_index: Any
                page_size: int
                data
                """
        _data = self.indexed_dataset()
        assert (index is not None and index >= 0) and index <= max(_data.keys())
        data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        for key, value in _data.items():
            if key >= start and data_count < page_size:
                data.append(value)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = key
                break
        pages = {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
        return pages
