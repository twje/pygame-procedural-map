from null_level import NullLevel
import utils


class LevelManager:
    def __init__(self, context):
        self.context = context
        self.levels = {}
        self.level_id = None
        self.add_level("null", NullLevel)
        self.set_level("null")

    def add_level(self, level_id, level):
        self.levels[level_id] = level(self)

    def set_level(self, level_id):
        self.level_id = level_id
        self.title = utils.create_text(level_id, 30)

    def handle_event(self, event):
        self.level.handle_event(event)

    def update(self, dt):
        self.level.update(dt)

    def draw(self, screen):
        self.level.draw(screen)
        screen.blit(self.title, dest=(0, 0))

    @property
    def level(self):
        return self.levels[self.level_id]
