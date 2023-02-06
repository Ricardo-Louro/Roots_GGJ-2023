import pygame, sys
from pygame.locals import *
from Functions import *

def Input_Manager(Player1, Player2):
    for event in pygame.event.get():
        if event.type == QUIT:
            Quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Quit()

            if event.key == K_d:
                if Player1.Angle < 0:
                    Player1.Angle = 0
                Player1.Angle += 1

            if event.key == K_a:
                if Player1.Angle > 0:
                    Player1.Angle = 0
                Player1.Angle -= 1

            if event.key == K_RIGHT:
                if Player2.Angle < 0:
                    Player2.Angle = 0
                Player2.Angle += 1

            if event.key == K_LEFT:
                if Player2.Angle > 0:
                    Player2.Angle = 0
                Player2.Angle -= 1