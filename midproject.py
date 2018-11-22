#!/usr/bin/python
# encoding: utf-8
### import area ###
import pygame
from pygame.locals import *
import random
import psychopy from visual, event

### parameters ###
screen_size = (800,600)
screen_center = (int(screen_size[0]/2),int(screen_size[1]/2))
back_ground_color = (0,0,0)
fullscreen_flag = False
guide_text1 = u"Please follow the guide line..."
guide_text2 = u"press space to continue"
state = 1 #1: guide 2:experiment 3:result
correct = 0
error = 0
counter = 10  #Do how many times?
Display_time = 500
Shape_Color  = [(255,0,0),(255,0,255),(0,255,0),(100,0,0),(145,100,0)] # Red,purple,green,blue,brown
Shape=['circle','square','triangle','pentagon','ellipse']
answer_flag = 0
pentagon_addr = [(screen_center[0]    ,screen_center[1]-50),
                 (screen_center[0]+50 ,screen_center[1]-5),
                 (screen_center[0]+30 ,screen_center[1]+50),
                 (screen_center[0]-30 ,screen_center[1]+50),
                 (screen_center[0]-50 ,screen_center[1]-5),]
#def function
def draw_shape(shape,color,screen):
    if shape == 'circle':
        pygame.draw.circle(screen, color, screen_center, 50, 0)
    elif shape == 'square':
        rect = pygame.Rect(0,0,100,100)
        rect.center = screen_center
        pygame.draw.rect(screen, color, rect, 0)
    elif shape == 'triangle':
        pygame.draw.polygon(screen, color, [(screen_center[0], screen_center[1]-50),
                                            (screen_center[0]-50, screen_center[1]+50),
                                            (screen_center[0]+50, screen_center[1]+50)], 0)
    elif shape == 'pentagon':
        pygame.draw.polygon(screen, color, pentagon_addr, 0)
    elif shape == 'ellipse':
        rect = pygame.Rect(0,0,130,80)
        rect.center = screen_center
        pygame.draw.ellipse(screen, color, rect, 0)
### main program ###

pygame.init()
if fullscreen_flag == True:
    screen = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(screen_size)
my_font = pygame.font.SysFont("simsunnsimsun", 32)
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if (event.key == K_SPACE) & (state == 1):
                state = 2
            if state == 4:
                if event.key == K_j: #yes
                    if rand_shape_1 == rand_shape_2:
                        correct += 1
                    else:
                        error +=1
                    state = 2
                elif event.key == K_f: #no
                    if rand_shape_1 == rand_shape_2:
                        error += 1
                    else:
                        correct +=1
                    state = 2
            if state == 5:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill(back_ground_color)
    
    if state == 1:
        name_surface = my_font.render(guide_text1, True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,screen_size[1]/2)))
        name_surface = my_font.render(guide_text2, True, (255,255,255))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,screen_size[1]-100)))
    elif state == 2:
        rand_color_1 = random.randint(0,4) #第一張圖顏色
        rand_shape_1 = random.randint(0,4) #第一張圖形狀
        rand_color_2 = random.randint(0,4) #第二張圖顏色
        rand_shape_2 = random.randint(0,4) #第二張圖形狀

        temp_random = random.randint(0,2) #增加圖形一樣機率
        if temp_random <= 1:
            rand_shape_2 = rand_shape_1
        print(counter)
        if counter == 0:
            state = 5
        else:
            state = 3
            counter -= 1
    elif state == 3:
        #draw first image
        name_surface = my_font.render('Here is experiment: 1st Image', True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,100)))
        draw_shape(Shape[rand_shape_1],Shape_Color[rand_color_1],screen)
        pygame.display.flip()
        pygame.time.wait(Display_time)
        #draw second image
        screen.fill(back_ground_color)
        name_surface = my_font.render('Here is experiment: 2nd Image', True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,100)))
        draw_shape(Shape[rand_shape_2],Shape_Color[rand_color_2],screen)
        pygame.display.flip()
        pygame.time.wait(Display_time)
        state = 4
    elif state == 4:
        name_surface = my_font.render('Are these 2 shape same?', True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,int(screen_size[1]*0.2))))
        name_surface = my_font.render('Yes -> J     No -> F', True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,int(screen_size[1]*0.5))))
    elif state == 5: #show result
        name_surface = my_font.render('Correct:' + str(correct) + '   Error:' + str(error), True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,int(screen_size[1]*0.2))))
        name_surface = my_font.render('Press any key to leave', True, (128,128,128))
        screen.blit(name_surface, name_surface.get_rect(center=(screen_size[0]/2,int(screen_size[1]*0.5))))
    pygame.display.flip()
pygame.quit()
