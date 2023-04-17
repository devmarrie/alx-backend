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
    values = []
    if page:
        for i in range(page_size + 1):
            values.append(i)
        return values[0], values[-1]
    

        
            