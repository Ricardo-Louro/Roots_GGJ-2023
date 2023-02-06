import time
from Functions import *

pygame.mixer.init()
Hit_Sound = pygame.mixer.Sound("Hit.wav")

pygame.font.init()
font = pygame.font.Font('Font.ttf', 500)

def End_Round_Screen(Screen, Backup, Player1, Player2):
    pygame.mixer.music.set_volume(0.5)
    Backup.blit(Screen, (0,0))

    Screen.fill((59,43,15))
    Player1_Score = font.render(str(Player1.Score), True, Player1.Colour)
    Player2_Score = font.render(str(Player2.Score), True, Player2.Colour)
    Screen.blit(Player1_Score, (200, 200))
    Screen.blit(Player2_Score, (1500, 200))
    pygame.display.flip()
    time.sleep(2)

    Screen.blit(Backup, (0,0))
    pygame.display.flip()

def Check_If_End_Game(Player1, Player2, PositionList, Screen, Backup, PlayerSpeed):
    Player1_Lost = False
    Player2_Lost = False

    if abs(Player1.Position[0]-Player2.Position[0]) + abs(Player1.Position[1] - Player2.Position[1]) < 5:
        Player1_Lost = True
        Player2_Lost = True

    for Value in PositionList:
        if abs(Player1.Position[0] - Value[0]) + abs(Player1.Position[1] - Value[1]) < PlayerSpeed:
            Player1_Lost = True

        if abs(Player2.Position[0] - Value[0]) + abs(Player2.Position[1] - Value[1]) < PlayerSpeed:
            Player2_Lost = True
    
    if Player1.Position[0] < 0 or Player1.Position[0] > 1920:
        Player1_Lost = True
    if Player1.Position[1] < 0 or Player1.Position[1] > 1080:
        Player1_Lost = True
    
    if Player2.Position[0] < 0 or Player2.Position[0] > 1920:
        Player2_Lost = True
    if Player2.Position[1] < 0 or Player2.Position[1] > 1080:
        Player2_Lost = True
        
    if Player1_Lost and Player2_Lost:
        Score("Draw", Player1, Player2)
        End_Round_Screen(Screen, Backup, Player1, Player2)
        return True
    elif Player1_Lost:
        Score("P2", Player1, Player2)
        End_Round_Screen(Screen, Backup, Player1, Player2)
        return True
    elif Player2_Lost:
        Score("P1", Player1, Player2)
        End_Round_Screen(Screen, Backup, Player1, Player2)
        return True
    else:
        return False


def Score(Winner, Player1, Player2):
    Player1.Speed = 0
    Player2.Speed = 0
    pygame.mixer.music.set_volume(0)
    pygame.mixer.Sound.play(Hit_Sound)
    time.sleep(1.5)
    
    if Winner == "Draw":
        Player1.Score += 1
        Player2.Score += 1

    elif Winner == "P2":
        Player2.Score += 1
    
    else:
        Player1.Score += 1