import universe
import display
import pygame

pygame.init()

myUniverse = universe.Universe()
myDisplay = display.Display([500,500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    msg = input()

    if msg == "p":
        myUniverse.paused = True
    elif msg == "r":
        myUniverse.paused = False
    else:
        myUniverse.simulate()