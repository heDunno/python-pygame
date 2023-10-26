import pygame
import sys
import random


pygame.init()

# Display
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption('flappy dunno')
#Font
font = pygame.font.Font('font/Pixeltype.ttf', 50)


#FPS
clock = pygame.time.Clock()

# Tube Defaults
# Tube 1
ran_tube_size = random.randint(115, 150)
ran_tube_size2 = random.randint(115, 170)
tube_surf_top = pygame.Surface((50,ran_tube_size))
tube_rect_top = tube_surf_top.get_rect(midtop = (350,0))
tube_surf_top.fill('Green')

tube_surf_bottom = pygame.Surface((50,130))
tube_rect_bottom = tube_surf_bottom.get_rect(midbottom = (350,400))
tube_surf_bottom.fill('Green')

#tube 2
tube_surf_top2 = pygame.Surface((50,115))
tube_rect_top2 = tube_surf_top2.get_rect(midtop = (600,0))
tube_surf_top2.fill('Green')

tube_surf_bottom2 = pygame.Surface((50,230))
tube_rect_bottom2 = tube_surf_bottom2.get_rect(midbottom = (600,400))
tube_surf_bottom2.fill('Green')

# background 
sky = pygame.image.load('FlappyBird/Sky.png').convert()
floor = pygame.image.load('FlappyBird/ground.png').convert()

# Plyer
plr_surf = pygame.Surface((20,15))
plr_rect = plr_surf.get_rect(center = (100,200))
plr_surf.fill('Red')
gravity = 0
# Others
score = 0
score_tube1 = False
score_tube2 = False
isAlive = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if isAlive and event.key == pygame.K_SPACE:
                gravity -= 5
            if not isAlive and event.key == pygame.K_SPACE:
                isAlive = True
                score = 0
                #reset everything
                plr_surf = pygame.Surface((20,15))
                plr_rect = plr_surf.get_rect(center = (100,200))
                plr_surf.fill('Red')
                gravity = 0
                tube_surf_top = pygame.Surface((50,130))
                tube_rect_top = tube_surf_top.get_rect(midtop = (350,0))
                tube_surf_top.fill('Green')

                tube_surf_bottom = pygame.Surface((50,130))
                tube_rect_bottom = tube_surf_bottom.get_rect(midbottom = (350,400))
                tube_surf_bottom.fill('Green')

                tube_surf_top2 = pygame.Surface((50,115))
                tube_rect_top2 = tube_surf_top2.get_rect(midtop = (600,0))
                tube_surf_top2.fill('Green')

                tube_surf_bottom2 = pygame.Surface((50,230))
                tube_rect_bottom2 = tube_surf_bottom2.get_rect(midbottom = (600,400))
                tube_surf_bottom2.fill('Green')


    if isAlive:
        
        screen.blit(sky, ((0,0)))
        
        #tube stuff
        # first tubes
        screen.blit(tube_surf_top,tube_rect_top)
        screen.blit(tube_surf_bottom,tube_rect_bottom)
        tube_rect_bottom.left -= 4
        tube_rect_top.left -= 4
        if tube_rect_bottom.right <= 0:
            tube_rect_bottom.left = 510
            tube_rect_top.left = 510
            # random size
            ran_tube_size = random.randint(115,160)
            ran_tube_size2 = random.randint(115,240)
            tube_surf_top = pygame.Surface((50,ran_tube_size))
            tube_surf_bottom= pygame.Surface((50,ran_tube_size2))
            tube_surf_bottom.fill('Green')
            tube_surf_top.fill('Green')
            tube_rect_top = tube_surf_top.get_rect(midtop = (520,0))
            tube_rect_bottom = tube_surf_bottom.get_rect(midbottom = (520,400))
            score_tube1 = False



        # 2nd pair of tubes
        # 2nd pair of tubes
        screen.blit(tube_surf_top2, tube_rect_top2)
        screen.blit(tube_surf_bottom2, tube_rect_bottom2)

        tube_rect_bottom2.left -= 4
        tube_rect_top2.left -= 4
        if tube_rect_bottom2.right <= 0:
            tube_rect_bottom2.left = 510
            tube_rect_top2.left = 510
            ran_tube_size = random.randint(115, 150)
            ran_tube_size2 = random.randint(115, 220)
            tube_surf_top2 = pygame.Surface((50, ran_tube_size))
            tube_surf_bottom2 = pygame.Surface((50, ran_tube_size2))
            tube_surf_bottom2.fill('Green')
            tube_surf_top2.fill('Green')
            tube_rect_top2 = tube_surf_top2.get_rect(midtop=(520, 0))
            tube_rect_bottom2 = tube_surf_bottom2.get_rect(midbottom=(520, 400))
            score_tube2 = False


        #ple
        plr_rect.y += gravity
        gravity += .2
        screen.blit(plr_surf, plr_rect)

        #points
        score_screen = font.render(f'{score}',False,'Blue')
        
        screen.blit(score_screen,(250,50))
        if not score_tube1 and tube_rect_bottom.midright  < (plr_rect.midleft):
            score+=1
            score_tube1 = True
        elif not score_tube2 and tube_rect_bottom2.midright  < plr_rect.midleft:
            score+=1
            score_tube2 = True
        #Collisions
        if plr_rect.bottom >= 300 or tube_rect_top.colliderect(plr_rect) or tube_rect_top2.colliderect(plr_rect) or tube_rect_bottom.colliderect(plr_rect) or tube_rect_bottom2.colliderect(plr_rect):
            isAlive = False
    elif not isAlive:
        font2 = pygame.font.Font('font/Pixeltype.ttf', 50)
        
        death_screen = font2.render(f'You Died! Score: {score}', False, 'Red')
        death_screen2 = font2.render(f'Click Space to restart',False, 'Red')
        death_rect2 = death_screen2.get_rect(center = (250,220))

        death_rect = death_screen.get_rect(center = (250,180))
        # o hide the score thats on top of screen i redraw everything
        screen.blit(sky, ((0,0)))
        screen.blit(tube_surf_top,tube_rect_top)
        screen.blit(tube_surf_bottom,tube_rect_bottom)
        screen.blit(tube_surf_top2, tube_rect_top2)
        screen.blit(tube_surf_bottom2, tube_rect_bottom2)
        screen.blit(plr_surf, plr_rect)

        screen.blit(death_screen2,death_rect2)

        screen.blit(death_screen,death_rect)
    screen.blit(floor,(0,300)) # all the way at end so tubes rnt over it

    pygame.display.update()   
    clock.tick(60)