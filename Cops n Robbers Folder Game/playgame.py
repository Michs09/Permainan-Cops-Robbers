import pygame,sys
pygame.init()
import random
import button
from pygame import mixer
import math
import gameover as o
clock = pygame.time.Clock()


# fungsi pause 
pause = True
def Unpaused():
        global pause
        pause = False


def Pause(screen):
        play_img = pygame.image.load("Assets/tombol/play.png").convert_alpha()
        play_button = button.Button(650, 300, play_img, 1)
        global pause
        pause = True
        while pause:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        if play_button.draw(screen):
                                Unpaused()
                                #pause = False
                pygame.display.update

def Gameplay(screen,latar):
        #inisiasi musik game play
        mixer.music.load("sounds/mainplay2.mp3")
        mixer.music.play(-1)

        # Menginisiasi image untuk button
        play_img = pygame.image.load("Assets/tombol/play.png").convert_alpha()
        pause_img = pygame.image.load("Assets/tombol/pause.png").convert_alpha()
        surrend_img = pygame.image.load("Assets/tombol/surrend.png").convert_alpha()

        # Menginisiasi tombol button
        pause_button = button.Button(650, 400, pause_img, 1)
        surrend_button2 = button.Button(650, 500, surrend_img, 0.5)


        # Score
        score_value = 1000
        font = pygame.font.Font('freesansbold.ttf', 32)

        # Pengkondisian level
        n = 30 
        m = 1
        target = 5000

        # Inisiasi score
        def show_score(x, y):
                score = font.render(str(score_value), True, ('black'))
                screen.blit(score, (x, y))

        # inisiasi player
        player_img = pygame.image.load("Assets/objek/player.png").convert_alpha()
        x1 = 300
        y1 = 300
        
        x1_change = 0       
        y1_change = 0

        def player(x,y):
                screen.blit(player_img,(x,y))

        
        # Pemunculan objek
        # list untuk spawn objek sumbu y
        objekA_Img = []
        objekAX = []
        objekAY = []
        objekAX_change = []
        objekAY_change = []
        num_of_objekA = 10
        ly3 = []

        # list untuk spawn objek sumbu x
        objekB_Img = []
        objekBX = []
        objekBY = []
        objekBX_change = []
        objekBY_change = []
        num_of_objekB = 10
        lx3 = []
        
        # inisiasi variabel dengan objek gambar
        money = 'Assets/objek/money.png'
        diamond = 'Assets/objek/diamond.png'
        treasure = 'Assets/objek/treasure.png'
        lock = 'Assets/objek/lock.png'
        handcuffs = 'Assets/objek/handcuffs.png'
        police = 'Assets/objek/police.png'

        ly = ['Assets/objek/treasure.png','Assets/objek/money.png','Assets/objek/diamond.png','Assets/objek/lock.png','Assets/objek/handcuffs.png','Assets/objek/police.png',]
        

        # spawn sumbu y
        for i in range(num_of_objekA):
                ly2 = random.choice(ly)
                objekA_Img.append(pygame.image.load(ly2)) # menampilkan objek yang ditampung dalam list
                objekAX.append(random.randrange(0, 550, 50))  # posisi menampilkan x
                objekAY.append(random.randrange(0, 600, 50)) # posisi menampilkan y
                objekAX_change.append(0)
                objekAY_change.append(4)

                ly3.append(ly2)

        def objekA(x, y, i):
                screen.blit(objekA_Img[i], (x, y)) 


        # spawn sumbu x
        lx = ['Assets/objek/treasure.png','Assets/objek/money.png','Assets/objek/diamond.png','Assets/objek/lock.png','Assets/objek/handcuffs.png','Assets/objek/police.png',]
        for j in range(num_of_objekB):
                lx2 = random.choice(lx)
                objekB_Img.append(pygame.image.load(lx2)) # menampilkan objek yang ditampung dalam list
                objekBX.append(random.randrange(0, 550, 50))  # posisi menampilkan x
                objekBY.append(random.randrange(0, 600, 50)) # posisi menampilkan y
                objekBX_change.append(4)
                objekBY_change.append(0)
                
                lx3.append(lx2)
        
        def objekB(x, y, i):
                screen.blit(objekB_Img[i], (x, y))
        

        # Fungsi untuk mendeteksi apakah objek mengenai player atau tidak
        def isCollision(objekX, objekY, playerX, playerY):
                distance = math.sqrt(math.pow(objekX - playerX, 2) + (math.pow(objekY - playerY, 2)))
                if distance < 50:
                        return True
                else:
                        return False



        # main loop game play
        run =  True
        while run:
                screen.blit(latar,(0,0))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() 
                                sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        x1_change = -10
                                        y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                        x1_change = 10
                                        y1_change = 0
                                elif event.key == pygame.K_UP:
                                        y1_change = -10
                                        x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                        y1_change = 10
                                        x1_change = 0
                        

                        # Pengkondisian score
                        if score_value > target:
                                n += 5
                                m += 2
                                target += 5000
                                                

                # Perubahan posisi player 
                x1 += x1_change
                y1 += y1_change
                if x1<0:
                        x1 = 0
                elif x1>550:
                        x1 = 550
                elif y1 > 550:
                        y1 = 550
                elif y1<0:
                        y1 = 0
                player(x1,y1)

                # Menampilkan button pada halaman permainan
                screen.blit(play_img,(650, 300))
                if pause_button.draw(screen):
                        Pause(screen)
                if surrend_button2.draw(screen):
                        mixer.music.load("sounds/gameover.mp3")
                        mixer.music.play()
                        o.akhir(screen,latar)
                               
        # Pergerakan objek
                for i in range(num_of_objekA):
                        objekAY[i] += objekAY_change[i]
                        if objekAY[i] <= 0:
                                objekAY_change[i] = 4
                                objekAX[i] += objekAX_change[i]

                        elif objekAY[i] >= 550:
                                objekAY_change[i] = -4
                                objekAX[i] += objekAX_change[i]
                        
                        collision = isCollision(objekAX[i], objekAY[i], x1, y1)
                        if collision:
                                untung = mixer.Sound("sounds/coin.mp3")
                                rugi = mixer.Sound("sounds/hit2.mp3")
                                if ly3[i] == money:
                                        score_value += 100
                                        untung.play()
                                elif ly3[i] == diamond:
                                        score_value += 300
                                        untung.play()
                                elif ly3[i] == treasure:
                                        score_value += 500
                                        untung.play()
                                elif ly3[i] == lock:
                                        score_value -= 200 * m
                                        rugi.play()
                                elif ly3[i] == handcuffs:
                                        score_value -= 400 * m
                                        rugi.play()
                                elif ly3[i] == police:
                                        score_value -= 600 * m
                                        rugi.play()
                                
                                #objekA_Img.remove[i]
                                objekAX[i] = random.randint(0, 550)
                                objekAY[i] = random.randrange(0,550,549)
                        objekA(objekAX[i], objekAY[i], i)
                

                # gerak objek sumbu y
                for i in range(num_of_objekB):
                        objekBX[i] += objekBX_change[i]
                        if objekBX[i] <= 0:
                                objekBX_change[i] = 4
                                objekBY[i] += objekBY_change[i]

                        elif objekBX[i] >= 550:
                                objekBX_change[i] = -4
                                objekBY[i] += objekBY_change[i]
                        
                        collision = isCollision(objekBX[i], objekBY[i], x1, y1)
                        if collision:
                                untung = mixer.Sound("sounds/coin.mp3")
                                rugi = mixer.Sound("sounds/hit2.mp3")
                                if lx3[i] == money:
                                        score_value += 100
                                        untung.play()
                                elif lx3[i] == diamond:
                                        score_value += 300
                                        untung.play()
                                elif lx3[i] == treasure:
                                        score_value += 500
                                        untung.play()
                                elif lx3[i] == lock:
                                        score_value -= 200 * m
                                        rugi.play()
                                elif lx3[i] == handcuffs:
                                        score_value -= 400 * m
                                        rugi.play()
                                elif lx3[i] == police:
                                        score_value -= 600 * m
                                        rugi.play()
                                
                                objekBX[i] = random.randrange(0,550,549)
                                objekBY[i] = random.randint(0, 550)
                        objekB(objekBX[i], objekBY[i], i)


                # Keadaan game Over
                if score_value <= 0:
                        mixer.music.load("sounds/gameover.mp3")
                        mixer.music.play()
                        o.akhir(screen,latar)


                # Menunjukkan score
                show_score(620, 190)
                pygame.display.update()

                # inisiasi waktu frame
                clock.tick(n)

        