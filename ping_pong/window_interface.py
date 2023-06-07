from pygame import display

from conf import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('ping-pong')
window.fill(BACKGROUND_COLOR)
