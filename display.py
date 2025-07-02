import pygame

class Display:
    screen = None
    sf = 1

    def __init__(self, size, ratio):
        self.screen = pygame.display.set_mode([size*ratio, size])

    def draw(self, particles):
        for p in particles:
            x = int(p.P[0] / self.sf)
            y = int(p.P[1] / self.sf)
            self.screen.blit(p.img, (x, y))

        pygame.display.flip()
        pygame.time.Clock().tick(20)
        self.screen.fill((0,0,0))