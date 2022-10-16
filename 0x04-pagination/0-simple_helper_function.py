#!/usr/bin/env python3
"""
index_range is a pagination function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    return (((page - 1) * page_size), (page * page_size))
