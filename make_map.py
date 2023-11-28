import pygame

class Map():
    def __init__(self, level_name, BLOCK_W, BLOCK_H, SCREEN_SIZE):
        self.level_name = level_name
        self.BLOCK_W = BLOCK_W
        self.BLOCK_H = BLOCK_H
        self.SCREEN_SIZE = SCREEN_SIZE
    

    def make_map(self):
        blocks = [pygame.Rect(x, y, self.BLOCK_W, self.BLOCK_H) 
          for x in range(0, self.SCREEN_SIZE[0], self.BLOCK_W)
          for y in range(0, self.SCREEN_SIZE[1] // 4, self.BLOCK_H)]
        return blocks