from pygame import transform, image
from pygame._sprite import Sprite
from pathlib import Path
from ping_pong.type_hints import *

from ping_pong.window_interface import window


class GameSprite(Sprite):
    def __init__(self, image_path: Path, sprite_position: SpriteCoordinates,
                 movement_velocity: int, sprite_size: SpriteSize) -> None:
        """
        Parent class for game sprites, used for visualisation of simple objects.
        :param image_path: path to sprite image.
        :param sprite_position: sprite start position (x, y).
        :param movement_velocity: amount of pixels sprite moves with.
        :param sprite_size: sprite size in pixels (width, height).
        """
        super().__init__()
        self.image = transform.scale(image.load(image_path), sprite_size)
        self.rect = self.image.get_rect()
        self.speed = movement_velocity
        self.rect.x = sprite_position[0]
        self.rect.y = sprite_position[1]

    def reset(self) -> None:
        """
        Blit sprite at it's current position.
        """
        window.blit(self.image, (self.rect.x, self.rect.y))
