import pygame
from Functions import *

pygame.font.init()
title_font = pygame.font.Font('Font.ttf', 500)
smaller_font = pygame.font.Font('Font.ttf', 100)

Title_Colour = (225,170,97)
BG_Colour = (59,43,15)

def Title_Screen(Screen):
    Screen.fill(BG_Colour)
    Title = title_font.render("Roots", True, Title_Colour)
    Text = smaller_font.render("Press any key to continue...", True, Title_Colour)
    Screen.blit(Title, (200, 40))
    Screen.blit(Text, (800, 700))
    pygame.display.flip()
    pygame.event.get()
    Wait_for_Input()
    Screen.fill(BG_Colour)