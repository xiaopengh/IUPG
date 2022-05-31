import pygame
import pytmx
import pyscroll

import dialog
from player import Player
from dialog import DialogBox

class Game:

    def __init__(self):
        # créer la fenêtre du jeu
        width, height = 800, 600
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("IUPG")

        # charger le map
        tmx_data1 = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data1 = pyscroll.TiledMapData(tmx_data1)
        map_layer1 = pyscroll.orthographic.BufferedRenderer(map_data1, self.win.get_size())
        map_layer1.zoom = 2

        tmx_data2 = pytmx.util_pygame.load_pygame('carte_dungeon.tmx')
        map_data2 = pyscroll.TiledMapData(tmx_data2)
        map_layer2 = pyscroll.orthographic.BufferedRenderer(map_data2, self.win.get_size())
        map_layer2.zoom = 2

        tmx_data3 = pytmx.util_pygame.load_pygame('carte_ile.tmx')
        map_data3 = pyscroll.TiledMapData(tmx_data3)
        map_layer3 = pyscroll.orthographic.BufferedRenderer(map_data3, self.win.get_size())
        map_layer3.zoom = 2

        tmx_data4 = pytmx.util_pygame.load_pygame('carte_house1.tmx')
        map_data4 = pyscroll.TiledMapData(tmx_data4)
        map_layer4 = pyscroll.orthographic.BufferedRenderer(map_data4, self.win.get_size())
        map_layer4.zoom = 2

        tmx_data5 = pytmx.util_pygame.load_pygame('carte_house2.tmx')
        map_data5 = pyscroll.TiledMapData(tmx_data5)
        map_layer5 = pyscroll.orthographic.BufferedRenderer(map_data5, self.win.get_size())
        map_layer5.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data1.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data1.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        self.dialog_box = DialogBox()

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer1, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal_enter_dungeon = tmx_data1.get_object_by_name('enter_dungeon')
        self.portal_rect_enter_dungeon = pygame.Rect(portal_enter_dungeon.x, portal_enter_dungeon.y,
                                                     portal_enter_dungeon.width, portal_enter_dungeon.height)

        portal_enter_ile = tmx_data1.get_object_by_name('sail_ile')
        self.portal_rect_enter_ile = pygame.Rect(portal_enter_ile.x, portal_enter_ile.y,
                                                 portal_enter_ile.width, portal_enter_ile.height)

        portal_enter_house1 = tmx_data1.get_object_by_name('enter_house1')
        self.portal_rect_enter_house1 = pygame.Rect(portal_enter_house1.x, portal_enter_house1.y,
                                                    portal_enter_house1.width, portal_enter_house1.height)

        portal_enter_house2 = tmx_data1.get_object_by_name('enter_house2')
        self.portal_rect_enter_house2 = pygame.Rect(portal_enter_house2.x, portal_enter_house2.y,
                                                    portal_enter_house2.width, portal_enter_house2.height)

        portal_exit_dungeon = tmx_data2.get_object_by_name('exit_dungeon')
        self.portal_rect_exit_dungeon = pygame.Rect(portal_exit_dungeon.x, portal_exit_dungeon.y,
                                                    portal_exit_dungeon.width, portal_exit_dungeon.height)

        portal_exit_ile = tmx_data3.get_object_by_name('exit_ile')
        self.portal_rect_exit_ile = pygame.Rect(portal_exit_ile.x, portal_exit_ile.y,
                                                portal_exit_ile.width, portal_exit_ile.height)

        portal_exit_house1 = tmx_data4.get_object_by_name('exit_house1')
        self.portal_rect_exit_house1 = pygame.Rect(portal_exit_house1.x, portal_exit_house1.y,
                                                   portal_exit_house1.width, portal_exit_house1.height)

        portal_exit_house2 = tmx_data5.get_object_by_name('exit_house2')
        self.portal_rect_exit_house2 = pygame.Rect(portal_exit_house2.x, portal_exit_house2.y,
                                                   portal_exit_house2.width, portal_exit_house2.height)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def switch_world_dungeon(self):
        # charger le map
        tmx_data1 = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data1 = pyscroll.TiledMapData(tmx_data1)
        map_layer1 = pyscroll.orthographic.BufferedRenderer(map_data1, self.win.get_size())
        map_layer1.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data1.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data1.get_object_by_name('enter_dungeon_exit')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer1, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal_enter_dungeon = tmx_data1.get_object_by_name('enter_dungeon')
        self.portal_rect_enter_dungeon = pygame.Rect(portal_enter_dungeon.x, portal_enter_dungeon.y,
                                                     portal_enter_dungeon.width, portal_enter_dungeon.height)

        portal_enter_ile = tmx_data1.get_object_by_name('sail_ile')
        self.portal_rect_enter_ile = pygame.Rect(portal_enter_ile.x, portal_enter_ile.y,
                                                 portal_enter_ile.width, portal_enter_ile.height)

        portal_enter_house1 = tmx_data1.get_object_by_name('enter_house1')
        self.portal_rect_enter_house1 = pygame.Rect(portal_enter_house1.x, portal_enter_house1.y,
                                                    portal_enter_house1.width, portal_enter_house1.height)

        portal_enter_house2 = tmx_data1.get_object_by_name('enter_house2')
        self.portal_rect_enter_house2 = pygame.Rect(portal_enter_house2.x, portal_enter_house2.y,
                                                    portal_enter_house2.width, portal_enter_house2.height)

    def switch_world_ile(self):
        # charger le map
        tmx_data1 = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data1 = pyscroll.TiledMapData(tmx_data1)
        map_layer1 = pyscroll.orthographic.BufferedRenderer(map_data1, self.win.get_size())
        map_layer1.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data1.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data1.get_object_by_name('sail_ile_exit')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer1, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal_enter_dungeon = tmx_data1.get_object_by_name('enter_dungeon')
        self.portal_rect_enter_dungeon = pygame.Rect(portal_enter_dungeon.x, portal_enter_dungeon.y,
                                                     portal_enter_dungeon.width, portal_enter_dungeon.height)

        portal_enter_ile = tmx_data1.get_object_by_name('sail_ile')
        self.portal_rect_enter_ile = pygame.Rect(portal_enter_ile.x, portal_enter_ile.y,
                                                 portal_enter_ile.width, portal_enter_ile.height)

        portal_enter_house1 = tmx_data1.get_object_by_name('enter_house1')
        self.portal_rect_enter_house1 = pygame.Rect(portal_enter_house1.x, portal_enter_house1.y,
                                                    portal_enter_house1.width, portal_enter_house1.height)

        portal_enter_house2 = tmx_data1.get_object_by_name('enter_house2')
        self.portal_rect_enter_house2 = pygame.Rect(portal_enter_house2.x, portal_enter_house2.y,
                                                    portal_enter_house2.width, portal_enter_house2.height)

    def switch_world_house1(self):
        # charger le map
        tmx_data1 = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data1 = pyscroll.TiledMapData(tmx_data1)
        map_layer1 = pyscroll.orthographic.BufferedRenderer(map_data1, self.win.get_size())
        map_layer1.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data1.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data1.get_object_by_name('enter_house1_exit')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer1, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal_enter_dungeon = tmx_data1.get_object_by_name('enter_dungeon')
        self.portal_rect_enter_dungeon = pygame.Rect(portal_enter_dungeon.x, portal_enter_dungeon.y,
                                                     portal_enter_dungeon.width, portal_enter_dungeon.height)

        portal_enter_ile = tmx_data1.get_object_by_name('sail_ile')
        self.portal_rect_enter_ile = pygame.Rect(portal_enter_ile.x, portal_enter_ile.y,
                                                 portal_enter_ile.width, portal_enter_ile.height)

        portal_enter_house1 = tmx_data1.get_object_by_name('enter_house1')
        self.portal_rect_enter_house1 = pygame.Rect(portal_enter_house1.x, portal_enter_house1.y,
                                                    portal_enter_house1.width, portal_enter_house1.height)

        portal_enter_house2 = tmx_data1.get_object_by_name('enter_house2')
        self.portal_rect_enter_house2 = pygame.Rect(portal_enter_house2.x, portal_enter_house2.y,
                                                    portal_enter_house2.width, portal_enter_house2.height)

    def switch_world_house2(self):
        # charger le map
        tmx_data1 = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data1 = pyscroll.TiledMapData(tmx_data1)
        map_layer1 = pyscroll.orthographic.BufferedRenderer(map_data1, self.win.get_size())
        map_layer1.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data1.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data1.get_object_by_name('enter_house2_exit')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer1, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal_enter_dungeon = tmx_data1.get_object_by_name('enter_dungeon')
        self.portal_rect_enter_dungeon = pygame.Rect(portal_enter_dungeon.x, portal_enter_dungeon.y,
                                                     portal_enter_dungeon.width, portal_enter_dungeon.height)

        portal_enter_ile = tmx_data1.get_object_by_name('sail_ile')
        self.portal_rect_enter_ile = pygame.Rect(portal_enter_ile.x, portal_enter_ile.y,
                                                 portal_enter_ile.width, portal_enter_ile.height)

        portal_enter_house1 = tmx_data1.get_object_by_name('enter_house1')
        self.portal_rect_enter_house1 = pygame.Rect(portal_enter_house1.x, portal_enter_house1.y,
                                                    portal_enter_house1.width, portal_enter_house1.height)

        portal_enter_house2 = tmx_data1.get_object_by_name('enter_house2')
        self.portal_rect_enter_house2 = pygame.Rect(portal_enter_house2.x, portal_enter_house2.y,
                                                    portal_enter_house2.width, portal_enter_house2.height)

    def switch_dungeon(self):
        # charger le map
        tmx_data2 = pytmx.util_pygame.load_pygame('carte_dungeon.tmx')
        map_data2 = pyscroll.TiledMapData(tmx_data2)
        map_layer2 = pyscroll.orthographic.BufferedRenderer(map_data2, self.win.get_size())
        map_layer2.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data2.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data2.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer2, default_layer=3)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data2.get_object_by_name('exit_dungeon')
        self.portal_rect_exit_dungeon = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

    def switch_ile(self):
        # charger le map
        tmx_data3 = pytmx.util_pygame.load_pygame('carte_ile.tmx')
        map_data3 = pyscroll.TiledMapData(tmx_data3)
        map_layer3 = pyscroll.orthographic.BufferedRenderer(map_data3, self.win.get_size())
        map_layer3.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data3.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data3.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer3, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data3.get_object_by_name('exit_ile')
        self.portal_rect_exit_ile = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

    def switch_house1(self):
        # charger le map
        tmx_data4 = pytmx.util_pygame.load_pygame('carte_house1.tmx')
        map_data4 = pyscroll.TiledMapData(tmx_data4)
        map_layer4 = pyscroll.orthographic.BufferedRenderer(map_data4, self.win.get_size())
        map_layer4.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data4.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data4.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer4, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data4.get_object_by_name('exit_house1')
        self.portal_rect_enter_house1 = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

    def switch_house2(self):
        # charger le map
        tmx_data5 = pytmx.util_pygame.load_pygame('carte_house2.tmx')
        map_data5 = pyscroll.TiledMapData(tmx_data5)
        map_layer5 = pyscroll.orthographic.BufferedRenderer(map_data5, self.win.get_size())
        map_layer5.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data5.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data5.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer5, default_layer=6)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data5.get_object_by_name('exit_house2')
        self.portal_rect_enter_house2 = pygame.Rect(portal.x, portal.y, portal.width, portal.height)

    def update(self):
        self.group.update()

        # vérification de l'entrée dans un portail dans carte principale
        if self.player.feet.colliderect(self.portal_rect_enter_dungeon):
            self.switch_dungeon()
        if self.player.feet.colliderect(self.portal_rect_enter_ile):
            self.switch_ile()
        if self.player.feet.colliderect(self.portal_rect_enter_house1):
            self.switch_house1()
        if self.player.feet.colliderect(self.portal_rect_enter_house2):
            self.switch_house2()
        if self.player.feet.colliderect(self.portal_rect_exit_dungeon):
            self.switch_world_dungeon()
        if self.player.feet.colliderect(self.portal_rect_exit_ile):
            self.switch_world_ile()
        if self.player.feet.colliderect(self.portal_rect_exit_house1):
            self.switch_world_house1()
        if self.player.feet.colliderect(self.portal_rect_exit_house2):
            self.switch_world_house2()

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
            self.dialog_box.render(self.win)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dialog_box.next_text()


        pygame.quit()
