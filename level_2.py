from typing import Text
import pygame
from map import Map


class Level2:
    def __init__(self, level_manager):
        self.level_manager = level_manager
        self.context = level_manager.context

        size = 16
        self.map = Map(
            self.context.screen_width()//size,
            self.context.screen_height()//size,
            size
        )
        self.map.generate(0)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.level_manager.set_level("level 1")

    def update(self, dt):
        pass

    def draw(self, screen):
        self.map.draw(screen)
