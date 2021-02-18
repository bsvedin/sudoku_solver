# Copyright Bryant Svedin (c) 17 Feb 2021.

import unittest
from collections import Counter

from entry import Entry
from group_type import GroupType


class TestEntry(unittest.TestCase):

    def test_update_possible_values_multiple_possible(self):
        # Given Unknown Entry
        entry = Entry(0, 0, 0)
        # When The possible values have more than one possible
        entry.initialize_possible_values([1, 2, 3, 4], GroupType.Row)
        entry.initialize_possible_values([2, 3, 4, 5], GroupType.Column)
        entry.initialize_possible_values([2, 4, 5], GroupType.Square)
        # Then The entry sets the 'All' possible values to the intersection of the three and does not set the value
        self.assertEqual(entry.possible_values[GroupType.All], [2, 4])
        self.assertEqual(entry.value, None)

    def test_update_possible_values_one_possible(self):
        # Given Unknown Entry
        entry = Entry(0, 0, 0)
        # When The possible values have only one possible intersection
        entry.initialize_possible_values([1, 2, 3, 4], GroupType.Row)
        entry.initialize_possible_values([2, 3, 5], GroupType.Column)
        entry.initialize_possible_values([2, 4, 5], GroupType.Square)
        # Then the value is set to the only possible value
        self.assertEqual(entry.value, 2)

    def test_update_possible_values_no_possible_throws_error(self):
        # Given Unknown Entry
        entry = Entry(0, 0, 0)
        # When The possible values have NO possible intersection
        # And the last possible type is updated
        entry.initialize_possible_values([1, 3, 4], GroupType.Row)
        entry.initialize_possible_values([2, 3, 5], GroupType.Column)
        # Then an error is raised
        with self.assertRaises(ValueError):
            entry.initialize_possible_values([2, 4, 5], GroupType.Square)

    def test_check_for_unique_possibility_has_one(self):
        # Given Unknown Entry with possibilities set
        entry = Entry(0, 0, 0)
        entry.initialize_possible_values([1, 2, 3, 4, 7], GroupType.Row)
        entry.initialize_possible_values([2, 3, 4, 5, 7], GroupType.Column)
        entry.initialize_possible_values([2, 4, 5, 7], GroupType.Square)
        # And the group possibilities have been counted
        # And the 7 only occurs once
        group_possibliities = [1, 2, 3, 1, 2, 4, 4, 3, 5, 7]
        counter = Counter(group_possibliities)
        # When The entry checks if it has a unique possible value
        entry.check_for_unique_possibility(counter)
        # Then the value is set to 7
        self.assertEqual(entry.value, 7)

    def test_check_for_unique_possibility_does_not_have_one(self):
        # Given Unknown Entry with possibilities set
        entry = Entry(0, 0, 0)
        entry.initialize_possible_values([1, 2, 3, 4, 7], GroupType.Row)
        entry.initialize_possible_values([2, 3, 4, 5, 7], GroupType.Column)
        entry.initialize_possible_values([2, 4, 5, 7], GroupType.Square)
        # And the group possibilities have been counted
        # And the 8 only occurs once but the entry does not have an 8 possibility
        group_possibliities = [1, 2, 3, 1, 2, 4, 7, 4, 3, 5, 7, 8]
        counter = Counter(group_possibliities)
        # When The entry checks if it has a unique possible value
        entry.check_for_unique_possibility(counter)
        # Then the value is set left None
        self.assertEqual(entry.value, None)

    def test_remove_impossible_values(self):
        # Given Unknown Entry with possibilities set
        entry = Entry(0, 0, 0)
        entry.initialize_possible_values([1, 2, 3, 4, 7], GroupType.Row)
        entry.initialize_possible_values([2, 3, 4, 5, 7], GroupType.Column)
        entry.initialize_possible_values([2, 4, 5, 7], GroupType.Square)
        # And the group duplicates have been counted
        impossible_values = [4]
        # When The entry removes the impossible values and there is only only possibility left
        entry.remove_impossible_values_duplicate(impossible_values)
        # Then the possible values are [2, 7]
        self.assertEqual(entry.possible_values[GroupType.All], [2, 7])
        self.assertEqual(entry.value, None)

    def test_remove_impossible_values_only_one_remains(self):
        # Given Unknown Entry with possibilities set
        entry = Entry(0, 0, 0)
        entry.initialize_possible_values([1, 2, 3, 4, 7], GroupType.Row)
        entry.initialize_possible_values([2, 3, 4, 5, 7], GroupType.Column)
        entry.initialize_possible_values([2, 4, 5, 7], GroupType.Square)
        # And the group duplicates have been counted
        impossible_values = [2, 4]
        # When The entry removes the impossible values and there is only only possibility left
        entry.remove_impossible_values_duplicate(impossible_values)
        # Then the value is set to 7
        # self.assertEqual(entry.possible_values[GroupType.All], [2, 4])
        self.assertEqual(entry.value, 7)


if __name__ == '__main__':
    unittest.main()
