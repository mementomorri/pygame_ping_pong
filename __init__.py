from pygame import *

from ping_pong.game_sprite import GameSprite
from ping_pong.racket import Racket
from ping_pong.conf import *
from ping_pong.window_interface import window
from ping_pong.type_hints import SpriteCoordinates, SpriteSize


run = True
game_over = False
game_pause = False
clock = time.Clock()
left_racket = Racket(RACKET_PATH, SpriteCoordinates(LEFT_RACKET_START_X, LEFT_RACKET_START_Y),
                     RACKET_SPEED, SpriteSize(RACKET_WIDTH, RACKET_HEIGHT))
right_racket = Racket(RACKET_PATH, SpriteCoordinates(RIGHT_RACKET_START_X, RIGHT_RACKET_START_Y),
                      RACKET_SPEED, SpriteSize(RACKET_WIDTH, RACKET_HEIGHT))
ball = GameSprite(BALL_PATH, SpriteCoordinates(BALL_START_X, BALL_START_Y),
                  BALL_SPEED, SpriteSize(BALL_SIZE, BALL_SIZE))
ball_direction_x = BALL_MOVE_DIRECTION_X
ball_direction_y = BALL_MOVE_DIRECTION_Y

font.init()
font = font.Font(None, 35)
win_p1 = [font.render('PLAYER 1 WINS!!!', True, FONT_COLOR), font.render('Press R to restart', True, FONT_COLOR)]
win_p2 = [font.render('PLAYER 2 WINS!!!', True, FONT_COLOR), font.render('Press R to restart', True, FONT_COLOR)]
pause_text = [font.render('PAUSE...', True, FONT_COLOR), font.render('Press P to continue', True, FONT_COLOR)]

if __name__ == '__main__':
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False
                if e.key == K_r:
                    game_over = False
                    ball.rect.x = BALL_START_X
                    ball.rect.y = BALL_START_Y
                    ball_direction_x = BALL_MOVE_DIRECTION_X
                    ball_direction_y = BALL_MOVE_DIRECTION_Y
                    left_racket.rect.x = LEFT_RACKET_START_X
                    left_racket.rect.y = LEFT_RACKET_START_Y
                    right_racket.rect.x = RIGHT_RACKET_START_X
                    right_racket.rect.y = RIGHT_RACKET_START_Y
                if e.key == K_p:
                    game_pause = not game_pause

        if game_pause:
            y = 200
            x = 260
            for line in pause_text:
                window.blit(line, (x, y))
                y += 50
                x -= 70

        if not game_over and not game_pause:
            window.fill(BACKGROUND_COLOR)
            left_racket.update_left_racket()
            right_racket.update_right_racket()
            ball.rect.x += ball_direction_x
            ball.rect.y += ball_direction_y

            if sprite.collide_rect(left_racket, ball) or sprite.collide_rect(right_racket, ball):
                ball_direction_x *= -1

            if ball.rect.y > WINDOW_HEIGHT - BALL_SIZE or ball.rect.y < 0:
                ball_direction_y *= -1

            if ball.rect.x < 0:
                game_over = True
                x = y = 200
                for line in win_p2:
                    window.blit(line, (x, y))
                    y += 50

            if ball.rect.x > WINDOW_WIDTH:
                game_over = True
                x = y = 200
                for line in win_p1:
                    window.blit(line, (x, y))
                    y += 50

            left_racket.reset()
            right_racket.reset()
            ball.reset()

        display.update()
        clock.tick(FPS)
