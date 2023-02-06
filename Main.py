import pygame, Classes
from Round import *
from pygame.locals import *

#Player1_Colours = [(194,192,68),(204,179,63),(179,141,68),(204,133,78),(194,98,76)]
#Player2_Colours = [(194,192,68),(204,179,63),(179,141,68),(204,133,78),(194,98,76)]

Player1_Colours = [(225,170,97),(219,137,29),(184,114,24),(158,99,20),(173,131,76)]
Player2_Colours = [(225,170,97),(219,137,29),(184,114,24),(158,99,20),(173,131,76)]

pygame.init()
pygame.mixer.music.load("Song.wav")
Screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
Backup = pygame.Surface((1920,1080))
pygame.display.set_caption("ROOTS - GGJ 2023")

pygame.mixer.music.play(-1,0,1000)
pygame.mixer.music.set_volume(0.5)

while True:
    Player1 = Classes.Player("LEFT", Player1_Colours, -0.5)
    Player2 = Classes.Player("RIGHT", Player2_Colours, 0.5)

    Main_Menu(Screen, Player1)
    
    while Player1.Score <3 and Player2.Score <3:
        Round(Screen, Backup, Player1, Player2)
    Final(Screen, Player1, Player2)