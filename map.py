from enum import Enum
import random
import pygame


class Tile(Enum):
    EMPTY = 0    
    WALL = 1
    FLOOR = 2


# colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Map:
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.grid = [None for _ in range(self.width * self.height)]

    def generate(self, seed):
        random.seed(seed)

        # init grid
        for i in range(self.width - 1):
            for j in range(self.height - 1):
                if ((i % 2 != 0) and (j % 2 != 0)):
                    self.set_tile(i, j, Tile.EMPTY)                    
                else:
                    self.set_tile(i, j, Tile.WALL)                    

        # carve out passages
        self.create_path(1, 1)

    def create_path(self, x, y):
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for index in range(4):
            dx = x + directions[index][0]
            dy = y + directions[index][1]
            if self.is_tile_valid(dx, dy):
                tile = self.get_tile(dx, dy)
                if tile == Tile.EMPTY:
                    # mark as tile floor
                    self.set_tile(dx, dy, Tile.FLOOR)

                    # knock down wall
                    ddx = x + directions[index][0] // 2
                    ddy = y + directions[index][1] // 2
                    self.set_tile(ddx, ddy, Tile.FLOOR)
                    
                    # recursive call
                    self.create_path(dx, dy)

    def is_tile_valid(self, x, y):
        return x > 0 and x < self.width and y > 0 and y < self.height

    def get_index(self, x, y):
        return x + self.width * y

    def get_tile(self, x, y):
        return self.grid[self.get_index(x, y)]

    def set_tile(self, x, y, tile):
        self.grid[self.get_index(x, y)] = tile

    def draw(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                x_pos = i * self.size
                y_pos = j * self.size
                index = self.get_index(i, j)
                if self.grid[index] == Tile.WALL:
                    pygame.draw.rect(screen, BLUE, (x_pos, y_pos, self.size, self.size))
                elif self.grid[index] == Tile.FLOOR:
                    pygame.draw.rect(screen, BLACK, (x_pos, y_pos, self.size, self.size))
                elif self.grid[index] == Tile.EMPTY:
                    pygame.draw.rect(screen, WHITE, (x_pos, y_pos, self.size, self.size))

