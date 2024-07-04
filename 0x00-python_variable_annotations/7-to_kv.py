#!/usr/bin/env python3
'''Includes to_kv function'''
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''
    returns a customized tuple
    '''

    return (k, v**2)
