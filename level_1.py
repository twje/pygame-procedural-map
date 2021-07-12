from typing import Text
import pygame
import utils


class Level1:
    def __init__(self, level_manager):
        self.level_manager = level_manager
        self.instructions = utils.create_text("Use keyboard arrow keys to traverse levels", 32)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.level_manager.set_level("level 2")

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.instructions, dest=(100, 50))
