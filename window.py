import pygame


class Window:
    def __init__(self, caption, width, height, event_callback):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.event_callback = event_callback
        self.is_done = False

    def destroy(self):
        pygame.quit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_done = True
            else:
                self.event_callback(event)

    def begin_draw(self):
        self.screen.fill((68, 85, 90))

    def end_draw(self):
        pygame.display.flip()
