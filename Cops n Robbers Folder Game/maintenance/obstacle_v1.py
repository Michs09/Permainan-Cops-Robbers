# Obstacle Generator, masih tahap pengembangan

import pygame, sys
from pygame.constants import K_ESCAPE, KEYDOWN
import random
from random import choice

pygame.init()

# layar = pygame.display.set_mode(size)
# img = pygame.image.load('path file') 
# pygame.image.load().convert() 
# pygame.image.load().convert_alpha()
# layar.blit(img, (x, y))
# pygame.display.update()
'''
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
'''
white = 255, 255, 255
layar = pygame.display.set_mode([800, 600])

bg = pygame.image.load('Assets/MAIN PAGE1.png')
char = pygame.image.load("Assets/player.png").convert_alpha()
        

def init():
    global d, komponen, num_a, num_b, num_r, num_l, score_0, t0, ta, kec, total, seq, urutan,  na_temp, nb_temp, nl_temp, nr_temp, t_temp, x_ob, y_ob
    t0 = 0
    ta = 0
    d = []
    score_0 = 2000
    num_a = 3 
    num_b = 2
    num_l = 4
    num_r = 3
    total = num_a + num_b + num_r + num_l
    na_temp = num_a 
    nb_temp = num_b
    nl_temp = num_l
    nr_temp = num_r
    t_temp = total
    kec = 1
    seq = 1
    urutan = 0
    banana = pygame.image.load("Assets/objek/banana.png")
    bom = pygame.image.load("Assets/objek/bom.png")
    diamond = pygame.image.load("Assets/objek/diamond.png")
    handcuffs = pygame.image.load("Assets/objek/handcuffs.png")
    lock = pygame.image.load("Assets/objek/lock.png")
    money = pygame.image.load("Assets/objek/money.png")
    police = pygame.image.load("Assets/objek/police.png")
    treasure = pygame.image.load("Assets/objek/treasure.png")
    
    komponen = [banana, bom, diamond, handcuffs, lock, money, police, treasure]
    
def main_char():
    global pos_x, pos_y, gerak
    pos_x, pos_y = 300, 300
    gerak = ''
    

def atas():
    global x_a, y_a, obs_a
    init()
    x_a = []
    y_a = 0
    obs_a = []
    for i in range(num_a):
        x_a.append(random.randrange(0, 570, 38))
        obs_a.append(choice(komponen))
    #print(len(obs_a))
    
def bawah():
    global x_b, y_b, obs_b
    init()
    x_b = []
    y_b = 600
    obs_b = []
    for i in range(num_b):
        x_b.append(random.randrange(0, 570, 38))
        obs_b.append(choice(komponen))
    
    
def kiri():
    global x_l, y_l, obs_l
    init()
    x_l = 0
    y_l = []
    obs_l = []
    for i in range(num_l):
        y_l.append(random.randrange(0, 579, 38))
        obs_l.append(choice(komponen))
    
def kanan():
    global x_r, y_r, obs_r
    init()
    x_r = 570
    y_r = []
    obs_r = []
    for i in range(num_r):
        y_r.append(random.randrange(0, 579, 38))
        obs_r.append(choice(komponen))
    

#for i in range(total): 
#pass

main_char()
atas()
bawah()
kiri()
kanan()

def database_obs(ob_a, ob_b, ob_l, ob_r, wn, x_char, y_char):
    global d
    d = []
    for i in range(ob_a):
        d.append([obs_a[i], x_a[i]])
    for j in range(ob_b):
        d.append([obs_b[j], x_b[j]])
    for k in range(ob_l):
        d.append([obs_l[k], y_l[k]])
    for l in range(ob_r):
        d.append([obs_r[l], y_r[l]])
    #print(len(d))
    position()
    condition(x_char, y_char)
    selection(wn)
    print(len(d))
    print(len(r_m))
    #print(score)

def position():
    global x_ob, y_ob, urutan
    x_ob, y_ob = [], []
    #seq = 0
    urutan = 0
    for i in d:
        if 0 < urutan <= na_temp:
            for j in i:
                if j == d[urutan][0]:
                    x_ob.append(d[urutan][1])
                    y_ob.append(y_a)
        if na_temp < urutan <= (na_temp+nb_temp):
            for j in i:
                if j == d[urutan][0]:
                    x_ob.append(d[urutan][1])
                    y_ob.append(y_b)
        if (na_temp+nb_temp) < urutan <= (na_temp+nb_temp+nl_temp):
            for j in i:
                if j == d[urutan][0]:
                    x_ob.append(x_l)
                    y_ob.append(d[urutan][1])
        if (na_temp+nb_temp+nl_temp) <= urutan <= t_temp:
            for j in i:
                if j == d[urutan][0]:
                    x_ob.append(x_r)
                    y_ob.append(d[urutan][1])
        #seq += 1
        urutan += 1

def selection(wn):
    global seq, urutan #x_ob, y_ob
    #x_ob, y_ob = [], []
    seq = 0 
    urutan = 0    
    for i in d:
        if 0 < urutan <= na_temp:
            for j in i:
                if j == d[urutan][0]:
                    wn.blit(j, (x_ob[seq], y_ob[seq]))
                    seq += 1
        if na_temp < urutan <= (na_temp+nb_temp):
            for j in i:
                if j == d[urutan][0]:
                    wn.blit(j, (x_ob[seq], y_ob[seq]))
                    seq += 1
        if (na_temp+nb_temp) < urutan <= (na_temp+nb_temp+nl_temp):
            for j in i:
                if j == d[urutan][0]:
                    wn.blit(j, (x_ob[seq], y_ob[seq]))
                    seq += 1
        if (na_temp+nb_temp+nl_temp) < urutan <= t_temp:
            for j in i:
                if j == d[urutan][0]:
                    wn.blit(j, (x_ob[seq], y_ob[seq]))
                    seq += 1
        urutan += 1
        
    
def dist(x_obj, y_obj, x_char, y_char):
    global r_m, distance, seq
    r_m = []
    distance = 0
    #seq = 0
    for n in range(t_temp):
        if 0 < n <= na_temp:
            distance = ((x_char - x_obj[n])**2 + (y_char - y_obj[n])**2)**0.5
            r_m.append(distance)
            distance = 0
        if na_temp < n <= (na_temp+nb_temp):
            distance = ((x_char - x_obj[n])**2 + (y_char - y_obj[n])**2)**0.5
            r_m.append(distance)
            distance = 0
        if (na_temp+nb_temp) < n <= (na_temp+nb_temp+nl_temp):
            distance = ((x_char - x_obj[n])**2 + (y_char - y_obj[n])**2)**0.5
            r_m.append(distance)
            distance = 0
        if (na_temp+nb_temp+nl_temp) < n <= t_temp:
            distance = ((x_char - x_obj[n])**2 + (y_char - y_obj[n])**2)**0.5
            r_m.append(distance)
            distance = 0

def condition(x_char, y_char):
    global index, na_temp, nb_temp, nl_temp, nr_temp, t_temp, d
    dist(x_ob, y_ob, x_char, y_char) # Sementara
    index = 0
    for r in r_m:
        if r <= 27:
            del d[index]
            if index < na_temp :
                na_temp -= 1
            if na_temp < index <= (na_temp+nb_temp):
                nb_temp -= 1
            if (na_temp+nb_temp) < index <= (na_temp+nb_temp+nl_temp):
                nl_temp -= 1
            if (na_temp+nb_temp+nl_temp) < index <= t_temp :
                nr_temp -= 1
        t_temp = na_temp+nb_temp+nl_temp+nr_temp
        index += 1
   
def scoring(scr):
    global score, pos_x, pos_y
    if str(d[index][0]) == 'banana':
        pos_x, pos_y = 300, 300
        del d[index]
    if str(d[index][0]) == 'diamond':
        scr += 300
        del d[index]
    if str(d[index][0]) == 'treasure':
        scr += 600
        del d[index]
    if str(d[index][0]) == 'police':
        scr -= 200
        del d[index]
    if str(d[index][0]) == 'handcuffs':
        scr -= 500
        del d[index]
    if str(d[index][0]) == 'lock':
        scr -= 300
        del d[index]
    if str(d[index][0]) == 'bom':
        scr -= 500
        del d[index]
    if str(d[index][0]) == 'money':
        scr += 100
        del d[index]
           

def path_obs(wn, x_char, y_char):
    global y_a, y_b, x_l, x_r
    
    database_obs(na_temp, nb_temp, nl_temp, nr_temp, wn, x_char, y_char)

    y_a += kec
    y_b -= kec
    x_l += kec
    x_r -= kec
    
    if y_a >= 600:
        y_a = 0
        atas()
    if y_b <= 0:
        y_b = 600
        bawah()
    if x_l >= 570:
        x_l = 0
        kiri()
    if x_r <= 0:
        x_r = 570
        kanan()


while True :
    
    layar.blit(bg, (0, 0))
    #layar.blit(char, (pos_x, pos_y))
    #path_obs(layar, pos_x, pos_y)
    
        
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gerak = 'kanan'
            elif event.key == pygame.K_LEFT:
                gerak = 'kiri'
            elif event.key == pygame.K_UP:
                gerak = 'atas'
            elif event.key == pygame.K_DOWN:
                gerak = 'bawah'
        
        if gerak == 'kanan':
            pos_x += 10
        elif gerak == 'kiri':
            pos_x -= 10
        elif gerak == 'atas':
            pos_y -= 10
        elif gerak == 'bawah':
            pos_y += 10
        
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 570:
            pos_x = 570
        elif pos_y < 0 :
            pos_y = 0
        elif pos_y > 570:
            pos_y = 570
        
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
    
    layar.blit(char, (pos_x, pos_y))
    path_obs(layar, pos_x, pos_y)
             
    pygame.display.update()
    

        
