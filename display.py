import pygame
class Display:
    screen = None

    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)

    def draw(self, particles):
        pass