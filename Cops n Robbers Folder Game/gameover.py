# Berisi sekumpulan baris menampung tampilan akhir / last page  
import pygame,sys
import button
import playgame as g
pygame.init()


def akhir(screen,latar):
        # game over page
        game_img = pygame.image.load("Assets/page/gameover.png").convert()
        ulang_img = pygame.image.load("Assets/tombol/restart.png").convert_alpha()
        exit_img = pygame.image.load("Assets/tombol/exit1.png").convert_alpha()

        # button game over
        exit_button2 = button.Button(400, 400, exit_img, 1)
        ulang = button.Button(200,400,ulang_img, 1)
        c = False
        while not c:
                for event in pygame.event.get(): 
                        screen.blit(game_img,(0,0))
                        if exit_button2.draw(screen):
                                pygame.quit()
                                sys.exit()
                        if ulang.draw(screen):
                               g.Gameplay(screen,latar) 
                        if event.type == pygame.QUIT:
                                pygame.quit() 
                                sys.exit()       
                pygame.display.update()