#!/usr/bin/env python3
'''Includes the function make_multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return a function that
    multiply a float by the multiplier
    '''
    def multiply(n: float) -> float:
        '''multiply a number
         by a multiplier
        '''

        return n * multiplier

    return multiply
