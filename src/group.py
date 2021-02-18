# Copyright Bryant Svedin (c) 17 Feb 2021.

import copy
from collections import Counter
from typing import List

from entry import Entry
from group_type import GroupType


class Group:
    def __init__(self, type: GroupType, group_number: int):
        self.entries: List[Entry] = []
        self.type = type
        self.group_number = group_number
        self.solved = False

    def initialize_possible_values(self) -> None:
        if self.solved:
            return
        possible_values = list(range(1, 10))
        for entry in self.entries:
            if entry.value is not None:
                possible_values.remove(entry.value)
        for entry in self.entries:
            entry.initialize_possible_values(possible_values, self.type)

    def update_possible_values(self) -> None:
        if self.solved:
            return
        values_in_group = []
        for entry in self.entries:
            if entry.value is not None:
                values_in_group.append(entry.value)
        for entry in self.entries:
            entry.remove_impossible_values(values_in_group)

    def _check_for_duplicate_possible_values(self):
        if self.solved:
            return
        entry_possible_value_sets_in_group = []
        for entry in self.entries:
            if entry.value is None:
                entry_possible_value_sets_in_group.append(copy.deepcopy(entry.possible_values[GroupType.All]))
        seen = {}
        duplicates = {}
        for values in entry_possible_value_sets_in_group:
            values = tuple(values)  # A list cannot be used as a dict key
            if seen.keys():
                if values in seen.keys():
                    duplicates[values] = 1
                    seen[values] += 1
                else:
                    seen[values] = 1
            else:
                seen[values] = 1
        for duplicate in duplicates.keys():
            duplicate = tuple(duplicate)
            if seen[duplicate] == len(duplicate):  # This checks if the length is e.g. 3 that 3 entries in the
                # group share the possibilities
                for entry in self.entries:
                    entry.remove_impossible_values_duplicate(duplicate)

    def _check_entries_for_unique_possible_values(self) -> None:
        if self.solved:
            return
        # self.update_possible_values()
        # Now check if there is a unique possible value for the entry
        all_possible_values = []
        for entry in self.entries:
            if entry.value is None:
                all_possible_values.extend(entry.possible_values[GroupType.All])
        counter = Counter(all_possible_values)
        for entry in self.entries:
            entry.check_for_unique_possibility(counter)

    def _check_group_for_unique_possibilities_in_other_groups(self):
        # This is to check that for example, if only row 2 in my square can have a 4 that it gets marked so that
        # row group can remove possibilities from other squares
        if self.type is GroupType.Square:
            all_possible_exclusives_in_group = []
            for entry in self.entries:
                if entry.value is None:
                    all_possible_exclusives_in_group.extend(entry.possible_values[GroupType.All])
            all_possible_exclusives_in_group = list(set(all_possible_exclusives_in_group))  # Get unique possibilities
            for value in all_possible_exclusives_in_group:
                rows_seen = []
                columns_seen = []
                for entry in self.entries:
                    if entry.value is None:
                        if value in entry.possible_values[GroupType.All]:
                            rows_seen.append(entry.row)
                            columns_seen.append(entry.column)
                rows_seen = list(set(rows_seen))  # Get unique possibilities
                columns_seen = list(set(columns_seen))  # Get unique possibilities
                if len(columns_seen) == 1 or len(rows_seen) == 1:
                    for entry in self.entries:
                        if entry.value is None:
                            if value in entry.possible_values[GroupType.All]:
                                entry.possible_values[GroupType.SquareExclusive][value] = self.group_number
        else:
            all_possible_exclusives_in_group = {}
            for entry in self.entries:
                if entry.possible_values[GroupType.SquareExclusive]:
                    for value in entry.possible_values[GroupType.SquareExclusive]:
                        if value in all_possible_exclusives_in_group:
                            all_possible_exclusives_in_group[value].append(entry.possible_values[GroupType.SquareExclusive][value])
                        else:
                            all_possible_exclusives_in_group[value] = [entry.possible_values[GroupType.SquareExclusive][value]]
                        # all_possible_exclusives_in_group[value] = entry.possible_values[GroupType.SquareExclusive][value]
                        # all_possible_exclusives_in_group.extend(entry.possible_values[GroupType.All])
            if all_possible_exclusives_in_group:
                for entry in self.entries:
                    entry.remove_impossible_values_exclusive_to_other_square(all_possible_exclusives_in_group)

    def _check_if_solved(self):
        if self.solved:
            return
        for entry in self.entries:
            if entry.value is None:
                self.solved = False
                return
        self.solved = True

    def solve(self):
        # Solve as much as possible
        if self.solved:
            return
        self.update_possible_values()
        self._check_for_duplicate_possible_values()
        self._check_entries_for_unique_possible_values()
        self._check_group_for_unique_possibilities_in_other_groups()
        self.update_possible_values()
        self._check_if_solved()
