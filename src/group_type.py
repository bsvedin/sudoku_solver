# Copyright Bryant Svedin (c) 17 Feb 2021.

from enum import Enum


class GroupType(Enum):
    Row = 'Row'
    Column = 'Column'
    Square = 'Square'
    SquareExclusive = 'SquareExclusive'
    All = 'All'
