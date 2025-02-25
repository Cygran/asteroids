import pygame
from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = (255, 255, 255)
        
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)