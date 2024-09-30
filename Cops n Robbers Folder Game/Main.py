# File Main.py
# Import modul
import pygame, sys
import button
import playgame as g
import gameover as o
from pygame import mixer
pygame.init()

# Membuat screen
size = [800,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("COPS N ROBBER")
icon = pygame.image.load('Assets/polmal.png')
pygame.display.set_icon(icon)

# inisiasi untuk musik home page
sound_homepage = mixer.music.load("sounds/opening.mp3")
mixer.music.play(-1)

# Load image
home = pygame.image.load("Assets/page/homepage.png").convert()
latar = pygame.image.load("Assets/page/main page.png").convert()
start_img = pygame.image.load("Assets/tombol/start.png").convert_alpha()
exit_img = pygame.image.load("Assets/tombol/exit1.png").convert_alpha()
info_img = pygame.image.load("Assets/tombol/info.png").convert_alpha()
close_img = pygame.image.load("Assets/tombol/close.png").convert_alpha()

# info load image
rog1 = pygame.image.load("Assets/page/rog1.png").convert()
rog2 = pygame.image.load("Assets/page/rog2.png").convert()
bleft_img = pygame.image.load("Assets/tombol/left.png").convert_alpha()
bright_img = pygame.image.load("Assets/tombol/right.png").convert_alpha()


#create button instances
start_button = button.Button(300, 175, start_img, 1)
info_button = button.Button(300, 275, info_img, 1)
exit_button = button.Button(300, 375, exit_img, 1)

# info page button
close_button = button.Button(670,100, close_img,1.5)
bleft = button.Button(100,460,bleft_img,1)
bright = button.Button(660,460,bright_img,1)



# info screen
def info():       
        def info1():
                a = False
                while not a:
                        for event in pygame.event.get():
                                screen.blit(rog2,(100,100))
                                if bleft.draw(screen):
                                        a = True
                                        info()
                                if bright.draw(screen):
                                        pass
                                if close_button.draw(screen):
                                        a = True
                                pygame.display.update()
        run =  False
        while not run:
                screen.blit(rog1,(100,100))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if bright.draw(screen):
                                run = True
                                info1()
                        if bleft.draw(screen):
                                run = True
                                info()
                        if close_button.draw(screen):
                                run = True
                        pygame.display.update()


# game loop
end = False
while not end:
    for event in pygame.event.get():
        screen.blit(home,(0,0))
        if start_button.draw(screen):
                sound_homepage = mixer.music.stop()
                g.Gameplay(screen,latar)
        if info_button.draw(screen):
                info()
        if exit_button.draw(screen):
                end = True
        if event.type == pygame.QUIT:
                end = True
    pygame.display.update()

pygame.quit()