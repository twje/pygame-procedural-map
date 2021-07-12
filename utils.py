import pygame


def create_text(text, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    return font.render(text, True, (255, 255, 255))
