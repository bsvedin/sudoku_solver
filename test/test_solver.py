# Copyright Bryant Svedin (c) 24 Feb 2021.

import unittest
from pathlib import Path

from solver import Solver


def solve(entries):
    solver = Solver(entries)
    solver.solve()
    return solver.get_solution()


class MyTestCase(unittest.TestCase):

    def test_easy_puzzle(self):
        entries = [[2, 5, 4, 6, 3, 0, 7, 0, 0],
                   [0, 1, 0, 0, 0, 2, 8, 0, 0],
                   [0, 0, 7, 9, 5, 1, 0, 4, 0],
                   [0, 7, 0, 0, 0, 0, 5, 8, 0],
                   [1, 6, 2, 0, 0, 9, 4, 0, 7],
                   [0, 3, 8, 7, 0, 0, 9, 0, 2],
                   [7, 2, 0, 3, 0, 0, 0, 0, 8],
                   [3, 0, 0, 8, 0, 0, 6, 0, 9],
                   [0, 9, 1, 0, 0, 0, 0, 0, 0],
                   ]

        solution = [[2, 5, 4, 6, 3, 8, 7, 9, 1],
                    [9, 1, 3, 4, 7, 2, 8, 6, 5],
                    [6, 8, 7, 9, 5, 1, 2, 4, 3],
                    [4, 7, 9, 1, 2, 3, 5, 8, 6],
                    [1, 6, 2, 5, 8, 9, 4, 3, 7],
                    [5, 3, 8, 7, 4, 6, 9, 1, 2],
                    [7, 2, 6, 3, 9, 4, 1, 5, 8],
                    [3, 4, 5, 8, 1, 7, 6, 2, 9],
                    [8, 9, 1, 2, 6, 5, 3, 7, 4],
                    ]
        self.assertEqual(solution, solve(entries))

    def test_hard_puzzle(self):
        entries = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
                   [0, 0, 0, 0, 7, 3, 0, 0, 9],
                   [3, 0, 9, 0, 0, 0, 0, 4, 5],
                   [4, 9, 0, 0, 0, 0, 0, 0, 0],
                   [8, 0, 3, 0, 5, 0, 9, 0, 2],
                   [0, 0, 0, 0, 0, 0, 0, 3, 6],
                   [9, 6, 0, 0, 0, 0, 3, 0, 8],
                   [7, 0, 0, 6, 8, 0, 0, 0, 0],
                   [0, 2, 8, 0, 0, 0, 0, 0, 0],
                   ]

        solution = [[1, 7, 2, 5, 4, 9, 6, 8, 3],
                    [6, 4, 5, 8, 7, 3, 2, 1, 9],
                    [3, 8, 9, 2, 6, 1, 7, 4, 5],
                    [4, 9, 6, 3, 2, 7, 8, 5, 1],
                    [8, 1, 3, 4, 5, 6, 9, 7, 2],
                    [2, 5, 7, 1, 9, 8, 4, 3, 6],
                    [9, 6, 4, 7, 1, 5, 3, 2, 8],
                    [7, 3, 1, 6, 8, 2, 5, 9, 4],
                    [5, 2, 8, 9, 3, 4, 1, 6, 7],
                    ]
        self.assertEqual(solution, solve(entries))

    def test_very_hard_puzzle(self):
        entries = [[4, 0, 0, 0, 9, 5, 0, 0, 0],
                   [1, 0, 0, 6, 0, 0, 8, 5, 2],
                   [2, 0, 0, 0, 0, 0, 0, 0, 7],
                   [0, 9, 0, 0, 0, 1, 0, 2, 0],
                   [0, 8, 0, 0, 0, 2, 9, 4, 0],
                   [0, 0, 0, 0, 5, 3, 0, 0, 0],
                   [9, 0, 3, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 4, 0, 0, 1, 7, 9],
                   [0, 0, 6, 1, 0, 0, 2, 0, 0],
                   ]

        solution = [[4, 7, 8, 2, 9, 5, 3, 6, 1],
                    [1, 3, 9, 6, 7, 4, 8, 5, 2],
                    [2, 6, 5, 3, 1, 8, 4, 9, 7],
                    [3, 9, 7, 8, 4, 1, 5, 2, 6],
                    [5, 8, 1, 7, 6, 2, 9, 4, 3],
                    [6, 2, 4, 9, 5, 3, 7, 1, 8],
                    [9, 1, 3, 5, 2, 7, 6, 8, 4],
                    [8, 5, 2, 4, 3, 6, 1, 7, 9],
                    [7, 4, 6, 1, 8, 9, 2, 3, 5]
                    ]
        self.assertEqual(solution, solve(entries))

    def test_very_hard_puzzle2(self):
        entries = [[6, 0, 0, 0, 0, 5, 0, 0, 0],
                   [0, 0, 0, 3, 0, 9, 0, 5, 0],
                   [0, 0, 0, 0, 4, 0, 0, 6, 0],
                   [4, 0, 3, 0, 0, 0, 0, 0, 0],
                   [0, 8, 0, 7, 0, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 1, 7, 0, 0],
                   [0, 0, 0, 0, 9, 0, 0, 0, 6],
                   [0, 0, 5, 0, 2, 0, 8, 4, 9],
                   [0, 4, 0, 0, 0, 3, 0, 0, 0],
                   ]

        solution = [[4, 7, 8, 2, 9, 5, 3, 6, 1],
                    [1, 3, 9, 6, 7, 4, 8, 5, 2],
                    [2, 6, 5, 3, 1, 8, 4, 9, 7],
                    [3, 9, 7, 8, 4, 1, 5, 2, 6],
                    [5, 8, 1, 7, 6, 2, 9, 4, 3],
                    [6, 2, 4, 9, 5, 3, 7, 1, 8],
                    [9, 1, 3, 5, 2, 7, 6, 8, 4],
                    [8, 5, 2, 4, 3, 6, 1, 7, 9],
                    [7, 4, 6, 1, 8, 9, 2, 3, 5]
                    ]
        self.assertEqual(solution, solve(entries))

    def test_hardest_puzzle(self):
        # Hardest puzzle according to a stack exchange I found
        entries = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 3, 6, 0, 0, 0, 0, 0],
                   [0, 7, 0, 0, 9, 0, 2, 0, 0],
                   [0, 5, 0, 0, 0, 7, 0, 0, 0],
                   [0, 0, 0, 0, 4, 5, 7, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 3, 0],
                   [0, 0, 1, 0, 0, 0, 0, 6, 8],
                   [0, 0, 8, 5, 0, 0, 0, 1, 0],
                   [0, 9, 0, 0, 0, 0, 4, 0, 0]]

        solution = [[8, 1, 2, 7, 5, 3, 6, 4, 9],
                    [9, 4, 3, 6, 8, 2, 1, 7, 5],
                    [6, 7, 5, 4, 9, 1, 2, 8, 3],
                    [1, 5, 4, 2, 3, 7, 8, 9, 6],
                    [3, 6, 9, 8, 4, 5, 7, 2, 1],
                    [2, 8, 7, 1, 6, 9, 5, 3, 4],
                    [5, 2, 1, 9, 7, 4, 3, 6, 8],
                    [4, 3, 8, 5, 2, 6, 9, 1, 7],
                    [7, 9, 6, 3, 1, 8, 4, 5, 2]
                    ]
        self.assertEqual(solution, solve(entries))

    def test_boards(self):
        boards_text = Path('../boards.txt').read_text()
        boards = [board for board in boards_text.splitlines() if not board.startswith('#') and board]
        number_solved = 0
        number_tried = 0
        for board in boards:
            entries = []
            while board:
                row, board = board[:9], board[9:]
                row = [int(val) for val in row]
                entries.append(row)
            solver = Solver(entries)
            try:
                number_tried += 1
                solver.solve()
                number_solved += 1
            except:
                pass
            print(solver.get_solution())
        print('Number Solved = ' + str(number_solved) + '/' + str(number_tried))


if __name__ == '__main__':
    unittest.main()
