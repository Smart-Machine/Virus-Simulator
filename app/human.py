import pygame as pg

class Human:
    def __init__(self, surface, x, y, radius=5, velocity=1, state=0, color='white'):
        self.surface = surface 
        self.x = x 
        self.y = y 
        self.radius = radius
        self.v_x = velocity * 0.3 
        self.v_y = velocity * 0.3
        self.state = state
        self.color = color

        self.set_state()

        self.min_width, self.min_height = 30, 30 
        self.max_width, self.max_height = 970, 470
        
    def draw(self):
        pg.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
    
    def move(self, simulation_speed):
        if self.x > self.max_width or self.x < self.min_width:
            self.v_x *= -1
        if self.y > self.max_height or self.y < self.min_height:
            self.v_y *= -1
        self.x += self.v_x * int(simulation_speed / 10)
        self.y += self.v_y * int(simulation_speed / 10)
    
    def set_state(self):
        if (self.state < 0):
            self.color = 'red' 
        else:
            self.color = self.color

