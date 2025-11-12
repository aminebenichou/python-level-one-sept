
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
squares = [
    {'start_coord':(0,0), 'end_coord':(190,190), 'x_checked':False, 'o_checked':False},
    {'start_coord':(200,0), 'end_coord':(390,190), 'x_checked':False, 'o_checked':False},
    {'start_coord':(400,0), 'end_coord':(590,190), 'x_checked':False, 'o_checked':False},
    {'start_coord':(0,200), 'end_coord':(190,390), 'x_checked':False, 'o_checked':False},
    {'start_coord':(200,200), 'end_coord':(390,390), 'x_checked':False, 'o_checked':False},
    {'start_coord':(400,200), 'end_coord':(590,390), 'x_checked':False, 'o_checked':False},
    {'start_coord':(0,400), 'end_coord':(190,590), 'x_checked':False, 'o_checked':False},
    {'start_coord':(200,400), 'end_coord':(390,590), 'x_checked':False, 'o_checked':False},
    {'start_coord':(400,400), 'end_coord':(590,590), 'x_checked':False, 'o_checked':False},
]
mouse_coord = None
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # checking for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord=pygame.mouse.get_pos()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    

    # RENDER YOUR GAME HERE
    for square in squares:
        pygame.draw.rect(screen, 'white', (square['start_coord'][0], square['start_coord'][1], 190,190))
        if square['o_checked']:
            pygame.draw.circle(screen, 'blue', (square['start_coord'][0]+95, square['start_coord'][1]+95), 50)
            pygame.draw.circle(screen, 'white', (square['start_coord'][0]+95, square['start_coord'][1]+95), 40)
        
        if mouse_coord!=None and  square['start_coord'][0]<mouse_coord[0]<square['end_coord'][0] and square['start_coord'][1]<mouse_coord[1]<square['end_coord'][1]:
            square['o_checked']=True
            mouse_coord=None
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()