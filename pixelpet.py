#################
### Libraries ###
#################

import pygame
from pygame import *
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
        r,b,r,b,b,b,b,b,
        r,b,r,b,b,b,g,g,
        b,b,b,b,b,b,g,g,
        r,b,r,b,b,g,g,g,
        b,b,b,b,b,g,b,g,
        b,b,b,g,b,g,w,g
        b,b,g,g,w,g,g,g,
        b,b,g,g,g,g,g,g
]

up3 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,g,g,g,g,b,b,
        b,g,w,g,g,w,g,b,
        b,g,b,g,g,b,g,b,
        b,g,g,g,g,l,g,b,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g
        ]

#######################
### Left Animations ###
#######################

left1 = [
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,g,g,g,g,e,e,
        e,e,g,w,g,w,g,e,
        e,g,g,e,g,e,g,e,
        e,g,g,g,g,g,g,e,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g
]


left2 = [
        g,g,g,g,g,g,g,g,
        e,g,g,g,g,g,g,g,
        e,g,e,g,g,e,g,g,
        e,e,g,g,g,g,e,e,
        e,e,e,g,g,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e
]
        
       
left3 = [
        e,y,e,e,e,e,y,e,
        e,e,e,y,e,y,e,y,
        y,e,g,g,g,g,e,e,
        e,g,w,g,e,g,g,e,
        e,g,e,g,w,g,g,e,
        e,g,g,g,g,g,g,e
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
]
        
        
        
########################
### Right Animations ###
########################
        
right1 = [
        e,e,g,g,g,g,g,e,
        e,g,e,g,g,e,g,e,
        e,g,b,g,g,b,g,g,
        e,g,g,g,g,g,g,e,
        e,e,g,g,g,e,e,e,
        r,b,b,b,b,r,b,b,
        o,o,r,o,r,o,r,r,
        r,o,o,o,o,o,o,o
]

right2 = [
	e,e,g,g,g,g,g,e,
        e,g,e,g,g,e,g,e,
        e,g,b,g,g,b,g,g,
        e,g,g,g,g,g,g,e,
        e,e,g,g,g,e,g,e,
        o,e,g,g,r,e,e,e,
        o,r,r,o,r,o,o,r,
        r,o,o,o,r,o,r,o	
]

right3 = [
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,g,g,e,e,e,
	e,e,g,g,g,g,e,e,
	r,g,g,g,g,r,g,e,
	o,o,o,r,o,r,o,o,
	r,o,o,o,r,r,o,r,
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
