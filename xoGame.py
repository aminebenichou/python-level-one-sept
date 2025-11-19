
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
turn = 0
my_font = pygame.font.Font(None, 50)
possibilities=[[0,1,2], [3,4,5], [6,7,8], [0,3,6], 
               [1,4,7], [2,5,8], [0,4,8], [2,4,6]]



def draw_o(square):
    if square['o_checked']:
        pygame.draw.circle(screen, 'blue', (square['start_coord'][0]+95, square['start_coord'][1]+95), 50)
        pygame.draw.circle(screen, 'white', (square['start_coord'][0]+95, square['start_coord'][1]+95), 40)



def draw_x(square):
    if square['x_checked']:
        first_line_start_pos= (square['start_coord'][0]+10, square['start_coord'][1]+10)
        first_line_end_pos= (square['end_coord'][0]-10, square['end_coord'][1]-10)
        second_line_start_pos=(square['end_coord'][0]-10, square['start_coord'][1]+10) # (x_end, y_start)
        second_line_end_pos=(square['start_coord'][0]+10, square['end_coord'][1]-10) # (x_start, y_end)
        
        pygame.draw.line(screen, 'red', first_line_start_pos, first_line_end_pos,10)
        pygame.draw.line(screen, 'red', second_line_start_pos, second_line_end_pos,10)


def exchanging(square, mouse_coord):
    if mouse_coord!=None and  square['start_coord'][0]<mouse_coord[0]<square['end_coord'][0] and square['start_coord'][1]<mouse_coord[1]<square['end_coord'][1]:
            if turn%2==0 and not square['x_checked']:
                square['o_checked']=True
            elif not square['o_checked']:
                square['x_checked']=True
            mouse_coord=None



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # checking for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord=pygame.mouse.get_pos()
            turn += 1
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    

    # RENDER YOUR GAME HERE
    for square in squares:
        pygame.draw.rect(screen, 'white', (square['start_coord'][0], square['start_coord'][1], 190,190))
          
        draw_o(square)
        
        draw_x(square)

        exchanging(square, mouse_coord)

    for possibility in possibilities:
        if squares[possibility[0]]['x_checked'] and squares[possibility[1]]['x_checked'] and squares[possibility[2]]['x_checked'] or (squares[possibility[0]]['o_checked'] and squares[possibility[1]]['o_checked'] and squares[possibility[2]]['o_checked']):
            text = my_font.render(f"You Won", True, 'red')
            screen.fill('black')
            screen.blit(text, (280,280))

            
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

pygame.quit()