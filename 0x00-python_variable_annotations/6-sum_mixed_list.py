#!/usr/bin/env python3
'''
Includes the function sum_mixed_list
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    return the sum of mix of ints and floats
    '''

    return sum(mxd_lst)
