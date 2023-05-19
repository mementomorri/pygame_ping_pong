from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WINDOW_HEIGHT - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WINDOW_HEIGHT - 150:
            self.rect.y += self.speed


BACKGROUND_COLOR = (200, 255, 255)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
FPS = 60
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(BACKGROUND_COLOR)

game = True
finish = False
clock = time.Clock()

racket1 = Player('data/racket.png', 30, 200, 4, 50, 150)
racket2 = Player('data/racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('data/tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

ball_direction_x = 3
ball_direction_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
            if e.key == K_r:
                finish = False
                ball.rect.x = 200
                ball.rect.y = 200
                ball_direction_x = 3
                ball_direction_y = 3

    if not finish:
        window.fill(BACKGROUND_COLOR)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += ball_direction_x
        ball.rect.y += ball_direction_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_direction_x *= -1

        if ball.rect.y > WINDOW_HEIGHT - 50 or ball.rect.y < 0:
            ball_direction_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > WINDOW_WIDTH:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
