# Copyright Bryant Svedin (c) 17 Feb 2021.

import unittest

from entry import Entry
from group import Group
from group_type import GroupType


class TestGroup(unittest.TestCase):

    def test_initialize_possible_values(self):
        # Given 9 Entries with starting values
        entries = [Entry(value=1, row=0, column=0),
                   Entry(value=2, row=0, column=1),
                   Entry(value=3, row=0, column=2),
                   Entry(value=0, row=0, column=3),
                   Entry(value=0, row=0, column=4),
                   Entry(value=0, row=0, column=5),
                   Entry(value=7, row=0, column=6),
                   Entry(value=8, row=0, column=7),
                   Entry(value=9, row=0, column=8),
                   ]
        group = Group(GroupType.Row, group_number=0)
        group.entries = entries
        group.initialize_possible_values()
        for entry in group.entries:
            if entry.value:
                self.assertEqual(entry.possible_values[GroupType.Row], [])
            else:
                self.assertEqual(entry.possible_values[GroupType.Row], [4, 5, 6])


if __name__ == '__main__':
    unittest.main()
