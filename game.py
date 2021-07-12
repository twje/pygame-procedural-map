from window import Window
from level_manager import LevelManager
from context import Context
import pygame


class Game:
    def __init__(self, width, height, caption):
        self.window = Window(width, height, caption, self.handle_event)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.elapsed_time = 0
        self.level_manager = LevelManager(Context(self.window.screen))

    def add_level(self, level_id, level):
        self.level_manager.add_level(level_id, level)

    def set_start_level(self, level_id):
        self.level_manager.set_level(level_id)

    def run(self):
        while not self.window.is_done:
            self.update()
            self.draw()
            self.restart_clock()

        self.destroy()

    def handle_event(self, event):
        self.level_manager.handle_event(event)

    def update(self):
        self.window.update()
        self.level_manager.update(self.elapsed_time)

    def draw(self):
        self.window.begin_draw()
        self.level_manager.draw(self.window.screen)
        self.window.end_draw()

    def restart_clock(self):
        self.elapsed_time = self.clock.tick(self.fps)/1000

    def destroy(self):
        self.window.destroy()
