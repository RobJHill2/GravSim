import universe
import display
import pygame

pygame.init()

myUniverse = universe.Universe()
size, ratio = int(input("size: ")), float(input("ratio: "))
myDisplay = display.Display(size, ratio)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myUniverse.paused = True

    if myUniverse.paused:
        command = input("-> ").split(" ")
        while command[0] != "play":
            if command[0] == "create":
                try:
                    m = float(command[1])
                    P = [float(command[2]), float(command[3])]
                    u = [float(command[4]), float(command[5])]
                except ValueError:
                    print("ERROR: BAD INPUT")
                except IndexError:
                    print("ERROR: BAD INPUT")
                else:
                    myUniverse.createParticle(m, P, u)

            command = input("-> ").split(" ")
        myUniverse.paused = False
    else:
        myUniverse.simulate()
        myDisplay.draw(myUniverse.particles)

pygame.quit()