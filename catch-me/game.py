import pygame
import random

pygame.init()
pygame.font.init()

FPS = 60
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(WHITE)

font = pygame.font.SysFont('Verdana', 26)

clock = pygame.time.Clock()


class Ball:
    def __init__(self, display):
        self.display = display
        self.radius = 30
        self.center_x = 100
        self.center_y = 100

        self.vx = 2
        self.vy = 2

    def show(self):
        pygame.draw.circle(display, BLUE, (self.center_x, self.center_y), self.radius)

    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy

    def clear(self):
        pygame.draw.circle(display, WHITE, (self.center_x, self.center_y), self.radius)

    def move(self):
        self.clear()
        self.go()
        self.show()

    def stop(self):
        self.vx = 0
        self.vy = 0

    def on_screen(self):
        x_sides = self.radius < self.center_x < WIDTH - self.radius
        y_sides = self.radius < self.center_y < HEIGHT - self.radius
        return x_sides and y_sides


class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)

        width, height = display.get_size()
        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)


class RandomPointMovingBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)

        self.vx = random.choice([-2, -1, 1, 2])
        self.vy = random.choice([-2, -1, 1, 2])


balls = []
for i in range(10):
    ball = RandomPointMovingBall(display)
    ball.show()
    balls.append(ball)

pygame.display.flip()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            counter = 0
            for ball in balls:
                ball.stop()

                if ball.on_screen():
                    counter += 1

            text = font.render('На экране осталось полных окружностей: ' + str(counter), True, (0, 0, 0))
            display.blit(text, (100, 150))
            print('На экране осталось полных окружностей:', counter)

    for ball in balls:
        ball.move()

    pygame.display.flip()
    clock.tick(FPS)