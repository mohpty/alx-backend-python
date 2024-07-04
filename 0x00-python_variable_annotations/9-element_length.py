#!/usr/bin/env python3
'''includes the function
element_length
'''
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return list of tuples
    '''
    return [(i, len(i)) for i in lst]
