import pygame, sys
from pygame.locals import *


def Quit():
    pygame.quit()
    sys.exit()

def Save_Positions(Position, List):
    List.append(Position)

def Wait_for_Input():
    Wait = True
    while Wait == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Quit()
                else:
                    Wait = False
                 
