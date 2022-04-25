import pygame
import pytmx
import pyscroll


class Game:

    def __init__(self):
        # créer la fênetre du jeu
        width, height = 800, 600
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("IUPG")

        # charger le map
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.win.get_size())
        map_layer.zoom = 2
        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        fps = 60
        pink = (255, 225, 255)
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(fps)
            # set frames per second

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.win.fill(pink)
            self.group.draw(self.win)
            pygame.display.flip()

        pygame.quit()
