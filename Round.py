from End_Game_Handler import *
from Input_Manager import *
from Functions import *

pygame.mixer.init()
Speed_Sound = pygame.mixer.Sound("Speed.wav")

title_font = pygame.font.Font('Font.ttf', 500)
smaller_font = pygame.font.Font('Font.ttf', 100)

BG_Colour = (59,43,15)

def Main_Menu(Screen, Player1):
    Screen.fill(BG_Colour)
    Title = title_font.render("Roots", True, Player1.Colour_Palette[0])
    Text = smaller_font.render("Press any key to continue...", True, Player1.Colour_Palette[0])
    Screen.blit(Title, (200, 40))
    Screen.blit(Text, (800, 700))
    pygame.display.flip()
    pygame.event.get()
    Wait_for_Input()
    Screen.fill(BG_Colour)

def Round(Screen, Backup, Player1, Player2):

    PositionList = []

    Timer = 0

    pygame.event.get()
    Player1.Reset_Values()
    Player2.Reset_Values()

    while True:
        Timer += 1
        Input_Manager(Player1, Player2)
        
        Player1.Rotate()
        Player2.Rotate()
        
        Player1.Move()
        Player2.Move()

        Player1.Render(Screen)
        Player2.Render(Screen)

        if Check_If_End_Game(Player1, Player2, PositionList, Screen, Backup, Player1.Speed):
            break

        Save_Positions(Player1.Position, PositionList)
        Save_Positions(Player2.Position, PositionList)

        if (Timer % 300 == 0):
            pygame.mixer.music.set_volume(0)
            pygame.mixer.Sound.play(Speed_Sound)
            Player1.Speed += 1
            Player2.Speed += 1
            pygame.mixer.music.set_volume(0.5)
            
        pygame.display.flip()
        pygame.time.Clock().tick(60)