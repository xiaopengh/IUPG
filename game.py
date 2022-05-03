import pygame
import pytmx
import pyscroll
from player import Player


class Game:

    def __init__(self):
        # créer la fênetre du jeu
        width, height = 800, 600
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("IUPG")

        # charger le map
        tmx_data = pytmx.util_pygame.load_pygame('carte_dungeon.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.win.get_size())
        map_layer.zoom = 2

        # générer un joueur
        player_position = tmx_data.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.player.move_up()
        elif pressed[pygame.K_a]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_s]:
            self.player.move_down()
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation('right')

    def run(self):
        fps = 60
        clock = pygame.time.Clock()
        running = True
        while running:

            clock.tick(fps)
            # set frames per second

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.win)
            self.handle_input()
            pygame.display.flip()

        pygame.quit()
