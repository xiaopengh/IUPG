import pygame
import pytmx
import pyscroll


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet_1 = pygame.image.load('./assets/huntress.png')
        self.sprite_sheet_2 = pygame.image.load('./assets/huntress_left.png')
        self.image = self.get_image(self.sprite_sheet_1, 50+8, 55)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 3
        self.images = {
            'left': self.get_image(self.sprite_sheet_2, 50+8, 55),
            'right': self.get_image(self.sprite_sheet_1, 50+8, 55)
        }
        self.old_position = self.position.copy()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, self.rect.height * 0.2)

    def save_location(self):
        self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey([0, 0, 0])

    def move_up(self): self.position[1] -= self.speed
    def move_down(self): self.position[1] += self.speed
    def move_right(self): self.position[0] += self.speed
    def move_left(self): self.position[0] -= self.speed

    def get_image(self, sheet, x, y):
        image = pygame.Surface([34, 42])
        image.blit(sheet, (0, 0), (x, y, 34, 42))
        return image
