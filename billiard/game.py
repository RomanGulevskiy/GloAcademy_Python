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

    def click_ball(self, x, y):
        x_sides = ball.center_x - ball.radius < x < ball.center_x + ball.radius
        y_sides = ball.center_y - ball.radius < y < ball.center_y + ball.radius
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


class BilliardBall(RandomPointMovingBall):
    def __init__(self, display):
        super().__init__(display)

    def go(self):
        super().go()

        if self.center_x <= self.radius or self.center_x >= WIDTH - self.radius:
            self.vx = -self.vx

        if self.center_y <= self.radius or self.center_y >= HEIGHT - self.radius:
            self.vy = -self.vy


def draw_text(display, text, x, y):
    font = pygame.font.SysFont('Verdana', 26)
    text_surface = font.render(text, True, (0, 0, 0))
    pygame.draw.rect(display,(255,255,255), (x, y, 50, 50))
    display.blit(text_surface, (x, y))


balls = []
for i in range(10):
    ball = BilliardBall(display)
    ball.show()
    balls.append(ball)

pygame.display.flip()

counter_top_border = 0
counter_bottom_border = 0
counter_left_border = 0
counter_right_border = 0
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for ball in balls:
        ball.move()

    for ball in balls:
        if ball.center_x - ball.radius <= 0:
            counter_left_border += 1
            draw_text(display, str(counter_left_border), 50, 270)
        elif ball.center_x + ball.radius >= WIDTH:
            counter_right_border += 1
            draw_text(display, str(counter_right_border), WIDTH - 50, 270)
        elif ball.center_y - ball.radius <= 0:
            counter_top_border += 1
            draw_text(display, str(counter_top_border), 400, 50)
        elif ball.center_y + ball.radius >= HEIGHT:
            counter_bottom_border += 1
            draw_text(display, str(counter_bottom_border), 400, HEIGHT - 50)

    pygame.display.update()
    clock.tick(FPS)