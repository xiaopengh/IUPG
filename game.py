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
        tmx_data = pytmx.util_pygame.load_pygame('carte_principale.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.win.get_size())
        map_layer.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data.get_object_by_name('enter_dungeon')
        self.portal_rect = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

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

    def switch_dungeon(self):
        # charger le map
        tmx_data = pytmx.util_pygame.load_pygame('carte_dungeon.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.win.get_size())
        map_layer.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data.get_object_by_name('exit_dungeon')
        self.portal_rect = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

    def switch_world(self):
        # charger le map
        tmx_data = pytmx.util_pygame.load_pygame('carte_principale.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.win.get_size())
        map_layer.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data.get_object_by_name('enter_dungeon')
        self.portal_rect = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

    def update(self):
        self.group.update()

        # vérifiaction de l'entrée dans un portail dans carte principale
        if self.player.feet.colliderect(self.portal_rect):
            self.switch_dungeon()


        # vérification de collision (comparer avec -1 pour savoir si la collision s'est passé)
        if self.player.feet.collidelist(self.walls) != -1:
            self.player.move_back()

    def run(self):
        fps = 60
        clock = pygame.time.Clock()
        running = True
        while running:

            # set frames per second
            clock.tick(fps)

            self.group.center(self.player.rect)
            self.group.draw(self.win)
            self.player.save_location()
            self.handle_input()
            self.update()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
