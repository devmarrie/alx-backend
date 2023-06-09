#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
         page, page_size
    Return:
          A tuple of size two (start index, end_index)
    """
    first = 0
    last = 0
    for _ in range(page):
        first = last
        last += page_size
    return first, last


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
        We read data from the  dataset function
         Args:
         page, page_size
         Return:
          A list of size two (start index, end_index)
        """
        dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # try fetching the data indexes
        try:
            indx = index_range(page, page_size)
            return dataset[indx[0]:indx[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Hypermedia pagination
        Returns:
               page_size: the length of the returned dataset page
               page: the current page number
               data: the dataset page (equivalent to return from previous task)
               next_page: number of the next page, None if no next page
               prev_page: number of the previous page,
                          None if no previous page
               total_pages: the total number of pages in the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        try:
            data = self.get_page(page, page_size)
            total_pages = int(len(self.dataset()) // page_size)
            next_page = page + 1 if page + 1 <= total_pages else None
            prev_page = page - 1 if page - 1 > 1 else None
            return {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
            }
        except IndexError:
            return {}
