import pygame
import time
from pygame.locals import *
import random

size = 40
limit = 0.2
class Apple():
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw_apple(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move_apple(self):
        self.x = random.randint(1, 20)*size
        self.y = random.randint(1, 18)*size


class Snake():
        def __init__(self, parent_screen, length):
            self.parent_screen = parent_screen
            self.image = pygame.image.load("resources/resources/block.jpg").convert()
            self.x = [360]*length
            self.y = [400]*length
            self.direction = 'u'
            self.length = length

        def move_l(self):
            self.direction = 'l'

        def move_r(self):
            self.direction = 'r'

        def move_d(self):
            self.direction = 'd'

        def move_u(self):
            self.direction = 'u'


        def walking(self):
                for i in range(self.length-1, 0, -1):
                    self.x[i] = self.x[i-1]
                    self.y[i] = self.y[i-1]
                if self.direction == 'l':
                    self.x[0] -= size
                if self.direction == 'r':
                    self.x[0] += size
                if self.direction == 'd':
                    self.y[0] += size
                if self.direction == 'u':
                    self.y[0] -= size

                self.draw()
        def draw(self):
            self.parent_screen.fill((100, 100, 100))
            for i in range(self.length):
                self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
            pygame.display.flip()

class Game:
        def __init__(self):
            pygame.init()
            pygame.mixer.init()
            self.surface = pygame.display.set_mode((1000, 800))
            self.snake = Snake(self.surface, 2)
            self.snake.draw()
            self.apple = Apple(self.surface)
            self.apple.draw_apple()
            sound = pygame.mixer.music.load("resources/resources/Naruto Theme Song.mp3")
            pygame.mixer.music.play(10)
        def render_background(self):
            bg = pygame.image.load("resources/resources/background.jpg")
            self.surface.blit(bg, (0, 0))
        def collision(self, x1, y1, x2, y2):
            if x2 <= x1 < x2 + size:
                if y2 <= y1 < y2 + size:
                    return True
            return False

        def display_score(self):
            font = pygame.font.SysFont('arial', 30)
            score = font.render(f"Score: {self.snake.length-2}", True, (200, 200, 200))
            self.surface.blit(score, (850, 10))


        def run(self):
                limit = 0.2
                running = True

                while running:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                              running = False
                            if event.key == K_RIGHT:
                                self.snake.move_r()
                            if event.key == K_LEFT:
                                self.snake.move_l()
                            if event.key == K_UP:
                                self.snake.move_u()
                            if event.key == K_DOWN:
                                self.snake.move_d()
                        elif event.type == QUIT:
                            running = False


                    self.render_background()
                    self.snake.walking()
                    self.apple.draw_apple()
                    self.display_score()
                    pygame.display.flip()
                    if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                        sound = pygame.mixer.Sound("resources/resources/believe_it.mp3")
                        pygame.mixer.Sound.play(sound)
                        limit -= 0.005
                        self.snake.length += 1
                        self.snake.x.append(-1)
                        self.snake.y.append(-1)
                        self.apple.move_apple()



                    for i in range(3, self.snake.length):
                        if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                            sound = pygame.mixer.Sound("resources/resources/1_snake_game_resources_crash.mp3")
                            pygame.mixer.Sound.play(sound)
                            print("game over")
                            print("YOUR SCORE IS")
                            print(self.snake.length-2)
                            exit(0)


                    time.sleep(limit)



if __name__ == '__main__':
    game = Game()
    game.run()
