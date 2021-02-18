# Copyright Bryant Svedin (c) 17 Feb 2021.

import copy
from math import floor
from typing import List

from group_type import GroupType


class Entry:

    def __init__(self, value: int, row: int, column: int):
        if value == 0:
            value = None
        self.value = value
        self.row = row
        self.column = column
        if row < 3:
            square_start_ind = 0
        elif row < 6:
            square_start_ind = 3
        else:
            square_start_ind = 6
        square_ind_add = floor(column/3)
        self.square = square_start_ind+square_ind_add
        self.possible_values = dict()
        self.initialize_possible_values_dictionary()

    def initialize_possible_values_dictionary(self):
        self.possible_values[GroupType.All] = []
        self.possible_values[GroupType.Row] = []
        self.possible_values[GroupType.Column] = []
        self.possible_values[GroupType.Square] = []
        self.possible_values[GroupType.SquareExclusive] = {}

    def initialize_possible_values(self, possible_values: List[int], type: GroupType):
        if self.value:
            return
        if not self.possible_values[type]:
            self.possible_values[type] = copy.deepcopy(possible_values)
        for value in self.possible_values[type]:
            if value not in possible_values:
                self.possible_values[type].remove(value)
        self._check_possible_values()

    def remove_impossible_values(self, values_in_group: List[int]):
        if self.value:
            return
        for value_in_group in values_in_group:
            self._remove_impossible_value(value_in_group)

    def remove_impossible_values_duplicate(self, impossible_values: List[int]):
        # The "impossible values duplicates" come from other entries in the group that have a small number of possible values that is identical with another entry
        # e.g. two different entries have possible values of [2, 3] and this entry is [2, 3, 4]
        # Therefore this entry must be 4 because the other two have to be 2 or 3
        if self.value:
            return
        if self.possible_values[GroupType.All] != list(impossible_values):
            for impossible_value in impossible_values:
                self._remove_impossible_value(impossible_value)

    def remove_impossible_values_exclusive_to_other_square(self, all_possible_exclusives_in_group):
        if self.value:
            return
        for value in all_possible_exclusives_in_group:
            if value in self.possible_values[GroupType.All]:
                exclusive_square = all_possible_exclusives_in_group[value]
                if len(exclusive_square) > 1 and len(set(exclusive_square)) == 1 and exclusive_square[0] != self.square:
                    # Then it occurs at least twice all in the same square that is not this square
                    self._remove_impossible_value(value)

    def _remove_impossible_value(self, value):
        if value in self.possible_values[GroupType.Row]:
            self.possible_values[GroupType.Row].remove(value)
        if value in self.possible_values[GroupType.Column]:
            self.possible_values[GroupType.Column].remove(value)
        if value in self.possible_values[GroupType.Square]:
            self.possible_values[GroupType.Square].remove(value)
        self._check_possible_values()

    def _check_possible_values(self) -> None:
        if self.value:
            return
        self.possible_values[GroupType.All] = list(set(self.possible_values[GroupType.Row]).intersection(self.possible_values[GroupType.Column]))
        self.possible_values[GroupType.All] = list(set(self.possible_values[GroupType.All]).intersection(self.possible_values[GroupType.Square]))
        if self.possible_values[GroupType.Row] and self.possible_values[GroupType.Column] and self.possible_values[GroupType.Square]:
            if len(self.possible_values[GroupType.All]) == 0:
                raise ValueError('Logic error somewhere in the code')
        if len(self.possible_values[GroupType.All]) == 1:
            self.value = self.possible_values[GroupType.All][0]
            self.initialize_possible_values_dictionary()

    def check_for_unique_possibility(self, group_possibility_count):
        if self.value:
            return
        for key in group_possibility_count:
            if group_possibility_count[key] == 1:
                if key in self.possible_values[GroupType.All]:
                    self.value = key
