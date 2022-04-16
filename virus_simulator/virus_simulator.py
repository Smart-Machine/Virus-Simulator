from distutils.log import error
import os
import random 
import sys
import datetime
import requests
from human import *

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame as pg

class App:

    """
        t    : switche themes
        r    : reset
        p    : pause
        q    : quit
        UP   : speed up   simulation
        DOWN : speed down simulation
    """

    def __init__(self):

        self.url = 'http://127.0.0.1:5000/data' 

        pg.init()
        pg.font.init()

        self.app_state = 1
        self.resolution = self.width, self.height = 1500, 500 
        self.surface = pg.display.set_mode(self.resolution)
        self.clock   = pg.time.Clock()

        self.background_color = 'black'
        self.frame_color = 'white'
        self.font_size = 25

        self.offset = 15
        self.simulation_area = pg.Rect(self.offset, self.offset, self.width - self.height - self.offset*2, self.height - self.offset*2)

        self.days = 1
        self.days_counter = 0
        self.simulation_speed = 10 

        self.speed_range = 7  
        self.radius = 3
        self.amount_of_humans = 1000 
        self.population = self.populate()

        self.cases = 1 

    
    def send_data(self, url, **data):
        response = requests.post(url, data = {
            'timestamp' : data['timestamp'],
            'cases'     : data['cases'] 
        })
        # print(f'Response status code: {response.status_code}')
        # print(f'Response text: {response.text}')


    def switch_theme(self):
        if (self.background_color == 'black'):
            self.background_color = 'white'
            self.frame_color = 'black'
            for p in self.population['healthy']:
                p.color = 'black'

        elif (self.background_color == 'white'):
            self.background_color = 'black'
            self.frame_color = 'white'
            for p in self.population['healthy']:
                p.color = 'white'

    
    def populate(self):
        population = {
            'healthy'  : [],
            'infected' : [],
            'recovered': []
        }

        for _ in range(self.amount_of_humans):
            c_x = random.randint(self.offset*2, self.width - self.height - self.offset*2)
            c_y = random.randint(self.offset*2, self.height - self.offset*2) 
            direction = random.choice([1, -1])
            velocity = direction * random.randint(1, self.speed_range)
            state = random.randint(-10, 100)
            human = Human(self.surface, c_x, c_y, self.radius, velocity, state)
            
            if (human.color == 'red'):
                population['infected'].append(human)

            elif (human.color == 'green'):
                population['recovered'].append(human)

            else:
                population['healthy'].append(human)

        return population 
    

    def generate_fonts(self, string, pos):
        font = pg.font.SysFont('freesanbold.ttf', self.font_size)
        text = font.render(string, True, self.frame_color)
        text_rect = text.get_rect()
        text_rect.center = pos #(1250, 250)
        return {'text': text, 'text_rect': text_rect}


    def draw(self):
        self.surface.fill(self.background_color)
        for k, v in self.population.items():
            for p in v:
                p.draw()
        pg.draw.rect(self.surface, self.frame_color, self.simulation_area, 2)
        self.surface.blit(self.time_font['text'], self.time_font['text_rect'])
        self.surface.blit(self.simulation_speed_font['text'], self.simulation_speed_font['text_rect'])
        self.surface.blit(self.healthy_font['text'], self.healthy_font['text_rect'])
        self.surface.blit(self.infected_font['text'], self.infected_font['text_rect'])
        self.surface.blit(self.recovered_font['text'], self.recovered_font['text_rect'])
    

    def update_time(self):
        if (self.days_counter % (101 - self.simulation_speed) == 0):
            self.days += 1
            self.days_counter = 0
        self.days_counter += 1


    def update(self, app_state):
        self.time_text = f"Days: {self.days}"
        self.time_font = self.generate_fonts(self.time_text, (1090, 30 + self.font_size * 0))

        self.simulation_speed_text = f"Simulation Speed {self.simulation_speed}"
        self.simulation_speed_font = self.generate_fonts(self.simulation_speed_text, (1090, 30 + self.font_size * 1))

        self.healthy_text = f"Healthy: {len(self.population['healthy'])}"
        self.healthy_font = self.generate_fonts(self.healthy_text, (1090, 30 + self.font_size * 2))

        self.infected_text = f"Infected: {len(self.population['infected'])}"
        self.infected_font = self.generate_fonts(self.infected_text, (1090, 30 + self.font_size * 3))

        self.recovered_text = f"Recovered: {len(self.population['recovered'])}"
        self.recovered_font = self.generate_fonts(self.recovered_text, (1090, 30 + self.font_size * 4))
        
        if (app_state > 0):
            for k, v in self.population.items():
                for p in v:
                    p.move(self.simulation_speed)
            self.update_time()
        
        self.cases += 1


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()

                    elif event.key == pg.K_p:
                        self.app_state *= -1

                    elif event.key == pg.K_r:
                        pg.quit()
                        self.__init__()

                    elif event.key == pg.K_t:
                        self.switch_theme()

                    elif event.key == pg.K_UP:
                        if self.simulation_speed + 10 <= 100:
                            self.simulation_speed += 10

                    elif event.key == pg.K_DOWN:
                        if self.simulation_speed - 10 > 0:
                            self.simulation_speed -= 10

            self.update(self.app_state)
            self.send_data(
                self.url, 
                timestamp = self.days,
                cases = self.cases
            )
            self.draw()

            pg.display.set_caption(f"Virus Simulator [FPS: {self.clock.get_fps():.0f}]")
            pg.display.flip()
            self.clock.tick(120)
 