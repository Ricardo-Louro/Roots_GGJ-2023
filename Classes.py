import pygame
import numpy
import random

class Player:
    Direction = pygame.Vector2(0,1)
    Speed = 3
    Score = 0
    Colour_Picker = -1

    def __init__(self, Position, Colour, Angle):
        self.Base_Angle = Angle
        self.Angle = self.Base_Angle
        self.Base_Position = Position
        self.Colour_Palette = Colour

    def Move(self):
        Normalized_Vector = self.Direction/numpy.linalg.norm(self.Direction)
        Velocity_Vector = numpy.multiply(self.Speed, Normalized_Vector)
        self.Position=numpy.add(self.Position,Velocity_Vector)

    def Rotate(self):
        self.Direction = self.Direction.rotate(self.Angle)
    
    def Render(self, screen):
        pygame.draw.circle(screen, self.Colour, self.Position, 5)

    def Reset_Values(self):
        if self.Base_Position == "LEFT":
            Which_Side = random.randint(0,1)
            if Which_Side == 0:
                self.Position = (random.randint(200,1000), 0)
                self.Direction = pygame.Vector2(0,1)
                self.Angle = self.Base_Angle
            if Which_Side == 1:
                self.Position = (0, random.randint(200,800))
                self.Direction = pygame.Vector2(1,0)
                self.Angle = 1

        elif self.Base_Position == "RIGHT":
            Which_Side = random.randint(0,1)
            if Which_Side == 0:
                self.Position = (random.randint(1200,1700), 0)
                self.Direction = pygame.Vector2(0,1)
                self.Angle = self.Base_Angle
            if Which_Side == 1:
                self.Position = (1920, random.randint(200,800))
                self.Direction = pygame.Vector2(-1,0)
                self.Angle = -1

        self.Speed = 3

        self.Colour_Picker += 1
        self.Colour = self.Colour_Palette[self.Colour_Picker]