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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myUniverse.paused = True

    if myUniverse.paused:
        msg = input()
        if msg == "play":
            myUniverse.paused = False
    else:
        myUniverse.simulate()
        myDisplay.draw(myUniverse.particles)