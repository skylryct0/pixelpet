#################
### Libraries ###
#################

import pygame
from pygame.locals import *
from sense_hat import SenseHat
import time

##################
### Initiation ###
##################

pygame.init()
pygame.display.set_mode((640, 480))
sense = SenseHat()
sense.clear()

###############
### Colours ###
###############

p = (204, 0 , 204) #pink
g = (0, 102, 102) #green
w = (255, 255, 255) #white
r = (255, 0, 0) #red
o = (255, 75, 75)
y = (204, 204, 0) #yellow
b = (0, 0, 0) #black

#######################
### Down Animations ###
#######################

down1 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,g,g,g,g,b,b,
        b,g,w,g,g,w,g,b,
        b,g,b,g,g,b,g,b,
        b,g,g,g,g,g,g,b,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g
        ]

down2 = [   
         b,b,b,b,b,b,b,b,                                                   
         b,b,b,b,b,b,b,b,                             
         b,b,g,g,g,g,b,b,                                          
         b,b,b,b,b,b,b,b,
         g,p,g,g,g,g,p,g,                                                  
         g,g,g,g,g,g,g,g,                                                    
         g,g,g,g,g,g,g,g 
            ]
down3 = [

        b,b,b,b,b,b,b,b,
        b,g,g,b,b,g,g,b,
        g,g,g,g,g,g,g,g,
        g,g,w,g,g,w,g,g,
        g,g,b,g,g,b,g,g,
        b,g,g,g,g,g,g,b,
        b,b,g,g,g,g,b,b,
        b,b,b,g,g,b,b,b
        ]


#####################
### Up Animations ###
#####################

up1 = [
        b,b,b,b,b,r,b,r,
        g,g,b,b,b,r,b,r,
        g,g,b,b,b,b,b,b,
        g,g,g,b,b,r,b,r,
        g,b,g,g,b,b,b,b,
        g,w,g,b,g,b,b,b,
        g,g,g,w,g,g,b,b,
        g,g,g,g,g,g,b,b
        ]

up2 = [
e,e,e,e,e,e,e,e,
e,p,e,e,e,e,e,e,
e,p,e,e,p,e,p,e,
e,p,g,g,p,y,y,e,
e,g,g,g,y,w,y,g,
e,g,g,g,g,y,y,e,
e,e,g,e,g,e,e,e,
e,e,e,e,e,e,e,e,
]

#######################
### Left Animations ###
#######################

left1 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,p,
p,e,p,e,e,e,p,e,
p,y,p,y,g,g,p,e,
e,g,w,y,g,g,g,e,
e,y,y,g,g,g,g,e,
e,e,g,e,g,e,g,e,
e,e,e,e,e,e,e,e,
]


left2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,p,e,
e,p,e,p,e,e,p,e,
e,y,p,y,g,g,p,e,
e,g,w,y,g,g,g,e,
e,y,y,g,g,g,g,e,
e,e,e,g,e,g,e,e,
e,e,e,e,e,e,e,e,
]

################
### Curses?? ### 
################

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                sense.clear()
                sense.set_pixels(move_right1)
                time.sleep(0.5)
                sense.set_pixels(move_right2)
                time.sleep(0.5)

        elif event.key == K_LEFT: 
                sense.clear()
                sense.set_pixels(move_left1)
                time.sleep(0.5)
                sense.set_pixels(move_left2)
                time.sleep(0.5)


        if event.type == QUIT:
            running = False
            print("CYA!!! <3")
