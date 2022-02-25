import pygame as pg
import random 
import sys
import datetime 

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
    
    def move(self):
        if self.x > self.max_width or self.x < self.min_width:
            self.v_x *= -1
        if self.y > self.max_height or self.y < self.min_height:
            self.v_y *= -1
        self.x += self.v_x 
        self.y += self.v_y
    
    def set_state(self):
        if (self.state < 0):
            self.color = 'red' 
        else:
            self.color = self.color

class App:
    def __init__(self):
        pg.init()
        pg.font.init()

        self.app_state = 1

        self.days = 1
        self.days_counter = 0
        self.simulation_speed = 1 

        self.resolution = self.width, self.height = 1500, 500 
        self.surface = pg.display.set_mode(self.resolution)
        self.clock   = pg.time.Clock()

        self.offset = 15
        self.simulation_area = pg.Rect(self.offset, self.offset, self.width - self.height - self.offset*2, self.height - self.offset*2)

        self.speed_range = 7 
        self.amount_of_humans = 10000 
        self.population = self.populate()

        self.font_size = 25
    
    def populate(self):
        population = {
            'healthy'  : [],
            'infected' : [],
            'recovered': []
        }
        radius = 1
        for _ in range(self.amount_of_humans):
            c_x = random.randint(self.offset*2, self.width - self.height - self.offset*2)
            c_y = random.randint(self.offset*2, self.height - self.offset*2) 
            direction = random.choice([1, -1])
            velocity = direction * random.randint(1, self.speed_range)
            state = random.randint(-10, 100)
            human = Human(self.surface, c_x, c_y, radius, velocity, state)
            if (state > 0):
                population['healthy'].append(human)
            else:
                population['infected'].append(human)
        return population 
    
    def generate_fonts(self, string, pos):
        font = pg.font.SysFont('freesanbold.ttf', self.font_size)
        text = font.render(string, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = pos #(1250, 250)
        return {'text': text, 'text_rect': text_rect}

    def draw(self):
        self.surface.fill('black')
        for k, v in self.population.items():
            for p in v:
                p.draw()
        pg.draw.rect(self.surface, 'white', self.simulation_area, 2)
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
                    p.move()
            self.update_time()

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
                    elif event.key == pg.K_UP:
                        if self.simulation_speed + 1 <= 100:
                            self.simulation_speed += 1
                    elif event.key == pg.K_DOWN:
                        if self.simulation_speed - 1 > 0:
                            self.simulation_speed -= 1

            self.update(self.app_state)
            self.draw()

            pg.display.set_caption(f"Virus Simulator [FPS: {self.clock.get_fps():.0f}]")
            pg.display.flip()
            self.clock.tick(120)
 
if __name__=='__main__':
    app = App()
    app.run()
