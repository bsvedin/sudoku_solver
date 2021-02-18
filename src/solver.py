# Copyright Bryant Svedin (c) 17 Feb 2021.

from typing import List

from entry import Entry
from group import Group
from group_type import GroupType


class Solver:

    def __init__(self, entries: List[List[int]]):
        self.solved = False
        self.rows: List[Group] = []
        self.columns: List[Group] = []
        self.squares: List[Group] = []
        for iter in range(0, 9):
            self.rows.append(Group(GroupType.Row, iter))
            self.columns.append(Group(GroupType.Column, iter))
            self.squares.append(Group(GroupType.Square, iter))
        self.entries: List[List[Entry]] = []
        # First convert all the entries to objects
        for row_number, row in enumerate(entries):
            row_entries = []
            for column_number, entry_value in enumerate(row):
                row_entries.append(Entry(entry_value, row_number, column_number))
            self.entries.append(row_entries)
        self._create_groups()

    def _create_groups(self):
        for row_number, row_entries in enumerate(self.entries):
            for column_number, entry in enumerate(row_entries):
                self.rows[row_number].entries.append(entry)
                self.columns[column_number].entries.append(entry)
                self.squares[entry.square].entries.append(entry)

    def initialize_possible_values(self):
        for row in self.rows:
            row.initialize_possible_values()
        for column in self.columns:
            column.initialize_possible_values()
        for square in self.squares:
            square.initialize_possible_values()

    def solve(self):
        iteration = 0
        self.initialize_possible_values()
        self._count_how_many_remain()
        while not self.solved:
            print('Interation = ' + str(iteration) + ' : Entries Unsolved = ' + str(self.number_remaining))
            self._print_puzzle()
            self._solve()
            self._check_if_solved()
            iteration += 1
            if iteration > 10:
                raise ArithmeticError('Should have solved it by now. Some logic missing')
        self._print_puzzle()

    def _solve(self):
        for row in self.rows:
            row.solve()
            self._update_possible_values()
        for column in self.columns:
            column.solve()
            self._update_possible_values()
        for square in self.squares:
            square.solve()
            self._update_possible_values()

    def _update_possible_values(self):
        for row in self.rows:
            row.update_possible_values()
        for column in self.columns:
            column.update_possible_values()
        for square in self.squares:
            square.update_possible_values()

    def _check_if_solved(self):
        squares_solved = True
        for square in self.squares:
            if not square.solved:
                squares_solved = False
        if squares_solved:
            self.solved = True
        self._count_how_many_remain()

    def _count_how_many_remain(self):
        self.number_remaining = 0
        for row in self.entries:
            for entry in row:
                if not entry.value:
                    self.number_remaining += 1

    def _print_puzzle(self):
        for row in self.entries:
            value = ''
            for entry in row:
                if entry.value:
                    value += str(entry.value) + ' | '
                else:
                    value += '  | '
            print(value)

    def get_solution(self) -> List[List[int]]:
        solution = []
        for row in self.entries:
            row_values = []
            for entry in row:
                row_values.append(entry.value)
            solution.append(row_values)
        return solution
