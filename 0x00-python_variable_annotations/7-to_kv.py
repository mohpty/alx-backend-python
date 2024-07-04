#!/usr/bin/env python3
'''Includes to_kv function'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    returns a customized tuple
    '''

    return (k, v**2)
