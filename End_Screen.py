import pygame, time

def End_Screen(Screen, Player1, Player2):
    pygame.font.init()
    font = pygame.font.Font('Font.ttf', 250)
    Final_Colour = (Player1.Colour[0]+50, Player1.Colour[1]+50, Player1.Colour[2]+50)
    
    if Player1.Score == 3 and Player2.Score == 3:
        Draw = font.render("Draw", True, Final_Colour)
        Screen.blit(Draw, (500, 700))
    
    elif Player1.Score == 3:
        P1_Win = font.render("Player One Wins", True, Final_Colour)
        Screen.blit(P1_Win, (200, 700))
    
    else:
        P2_Win = font.render("Player Two Wins", True, Final_Colour)
        Screen.blit(P2_Win, (200, 700))
    
    pygame.display.flip()
    time.sleep(3)