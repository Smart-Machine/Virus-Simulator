import os
import random

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame as pg
from pygame.surface import Surface 

class Human:

    """
            [Colors]
        White -> Susceptible
        Red -> Infected
        Blue -> Recovered
        Black -> Dead

            [State]
        'Susceptible'
        'Infected'
        'Recovered'
        'Dead'
    """

    def __init__(
        self, 
        surface: Surface, 
        x: int, y: int, 
        radius: int = 5, 
        velocity: int = 1, 
        state: int = 0, 
        color: str = 'white',
        time: int = 7
    ) -> None:

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

        self.recovered_time = time 
        

    def draw(self) -> None:

        pg.draw.circle(
            self.surface, 
            self.color, 
            (self.x, self.y), 
            self.radius
        )
    

    def move(self, simulation_speed: int) -> None:

        if self.x > self.max_width or self.x < self.min_width:
            self.v_x *= -1

        if self.y > self.max_height or self.y < self.min_height:
            self.v_y *= -1
        
        self.x += self.v_x * int(simulation_speed / 10)
        self.y += self.v_y * int(simulation_speed / 10)
    

    def set_state(self) -> None:

        if self.state == 'susceptible':
            return 
        elif self.state == 'infected':
            self.color = 'red' 
        elif self.state == 'recovered':
            self.color = 'blue'
        elif self.state == 'dead':
            self.color = 'black'

