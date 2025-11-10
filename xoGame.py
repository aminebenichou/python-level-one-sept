
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    pygame.draw.rect(screen, 'white', (0,0, 190,190))
    pygame.draw.rect(screen, 'white', (0,200, 190,190))
    pygame.draw.rect(screen, 'white', (0,400, 190,190))

    pygame.draw.rect(screen, 'white', (200,0, 190,190))
    pygame.draw.rect(screen, 'white', (200,200, 190,190))
    pygame.draw.rect(screen, 'white', (200,400, 190,190))

    pygame.draw.rect(screen, 'white', (400,0, 190,190))
    pygame.draw.rect(screen, 'white', (400,200, 190,190))
    pygame.draw.rect(screen, 'white', (400,400, 190,190))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()