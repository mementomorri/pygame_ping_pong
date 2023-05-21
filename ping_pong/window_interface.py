from pygame import display

from ping_pong.conf import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(BACKGROUND_COLOR)
