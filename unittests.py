# -*- coding: utf-8 -*-

import unittest
from sudoku import Grid

class SudokuTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_4x4(self):
        g = Grid(4,2,{(4,1,3),(3,2,1),(3,3,3),(2,3,2),(1,4,4)})
        g.solve()
        self.assertEqual(g.grid,
        [[0, 0, 0, 0, 0],
         [0, 2, 3, 1, 4],
         [0, 1, 4, 2, 3],
         [0, 4, 1, 3, 2],
         [0, 3, 2, 4, 1]])
         
        g = Grid(4,2,{(2,1,2),(1,2,4),(2,3,4),(3,4,3),(4,3,1)})
        g.solve()
        self.assertEqual(g.grid,
        [[0, 0, 0, 0, 0],
         [0, 1, 4, 3, 2],
         [0, 2, 3, 4, 1],
         [0, 4, 1, 2, 3],
         [0, 3, 2, 1, 4]])
        
        g = Grid(4,2,{(1,1,3),(4,1,4),(2,2,2),(3,3,4),(4,4,1)})
        g.solve()
        self.assertEqual(g.grid,
        [[0, 0, 0, 0, 0],
         [0, 3, 4, 1, 2],
         [0, 1, 2, 3, 4],
         [0, 2, 1, 4, 3],
         [0, 4, 3, 2, 1]])
         
if __name__ == '__main__':
    unittest.main()