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
        values_in_group = [entry.value for entry in self.entries if entry.value]
        for entry in self.entries:
            entry.remove_impossible_values(values_in_group)

    def _check_for_naked_twin_possible_values(self):
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
            if seen[duplicate] == len(duplicate):
                # This checks if the length is e.g. 3 that 3 entries in the group share the possibilities
                for entry in self.entries:
                    entry.remove_impossible_values_from_naked_twins(duplicate)

    def _check_entries_for_unique_possible_values(self) -> None:
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
            if all_possible_exclusives_in_group:
                for entry in self.entries:
                    entry.remove_impossible_values_exclusive_to_other_square(all_possible_exclusives_in_group)

    def _check_for_hidden_twins(self):
        # First check all the possible values and how many times they are seen and where they were seen
        all_possible_values_in_group = {}
        for index, entry in enumerate(self.entries):
            for value in entry.possible_values[GroupType.All]:
                if value in all_possible_values_in_group:
                    all_possible_values_in_group[value]['seen'] += 1
                    all_possible_values_in_group[value]['where'].append(index)
                else:
                    all_possible_values_in_group[value] = {}
                    all_possible_values_in_group[value]['seen'] = 1
                    all_possible_values_in_group[value]['where'] = [index]
        # Check if any of them are only seen twice
        possible_hidden_pair_values = []
        possible_hidden_pair_positions = []
        for value in all_possible_values_in_group:
            if all_possible_values_in_group[value]['seen'] == 2:
                possible_hidden_pair_values.append(value)
                possible_hidden_pair_positions.append(all_possible_values_in_group[value]['where'])
        hidden_pairs = []
        for first_value, positions in zip(possible_hidden_pair_values, possible_hidden_pair_positions):
            if possible_hidden_pair_positions.count(positions) == 2:
                for second_value, second_positions in zip(possible_hidden_pair_values, possible_hidden_pair_positions):
                    if second_positions == positions and first_value != second_value:
                        pair = [first_value, second_value]
                        pair.sort()
                        hidden_pairs.append(tuple(pair))
        if hidden_pairs:
            hidden_pairs = list(set(hidden_pairs))
            for hidden_pair in hidden_pairs:
                for entry in self.entries:
                    entry.remove_impossible_values_from_hidden_twins(hidden_pair)

    def _check_for_naked_chains(self):
        # IMPLEMENT ME!
        pass

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
        self._check_for_naked_twin_possible_values()
        self._check_entries_for_unique_possible_values()
        self._check_group_for_unique_possibilities_in_other_groups()
        self._check_for_hidden_twins()
        self.update_possible_values()
        self._check_if_solved()
