#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


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
    

        
            