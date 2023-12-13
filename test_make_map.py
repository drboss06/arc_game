import unittest
from make_map import Map
import pygame

class TestMakeMap(unittest.TestCase):
    def test_make_map(self):
        # Make Map object
        map = Map("level1", 10, 10, (800, 600))

        # call make_map
        blocks = map.make_map()

        # The result should be a list of pygame.Rect objects
        self.assertIsInstance(blocks, list)

        # Every object is a pygame.Rect
        for block in blocks:
            self.assertIsInstance(block, pygame.Rect)

        # List of blocks is not empty
        self.assertNotEqual(len(blocks), 0)
        

if __name__ == '__main__':
    unittest.main()